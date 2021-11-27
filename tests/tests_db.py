import json

import pytest

from pysondb.db import (getDb, DataNotFoundError, IdNotFoundError,
                        SchemaError)

ID_FIXTURE = {"data": [{"id": 9999999999, "name": "test"}]}
ID_FIXTURE_STR = json.dumps(ID_FIXTURE)
EMPTY_FIXTURE_STR = json.dumps({"data": []})


def test_database_add(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(EMPTY_FIXTURE_STR)
    a = getDb(file.strpath)
    x = a.add({"name": "test"})
    assert int(x)


def test_database_add_many(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(EMPTY_FIXTURE_STR)
    a = getDb(file.strpath)
    a.addMany([{"name": "test"}, {"name": "test2"}])
    data = a.getAll()
    assert len(data) == 2
    for d in data:
        assert int(d["id"])


def test_database_get(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(EMPTY_FIXTURE_STR)
    a = getDb(file.strpath)
    fixture = [
        {"name": "test", "getbyfield": "row1"},
        {"name": "test works!", "getbyfield": "row2"},
        {"name": "testing, so much fun .. yeah.", "getbyfield": "row3"},
    ]
    a.addMany(fixture)
    assert len(a.get(1)) == 1
    assert len(a.get(2)) == 2
    assert len(a.get(3)) == 3


def test_database_get_by(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(EMPTY_FIXTURE_STR)
    a = getDb(file.strpath)
    fixture = [
        {"name": "test", "getbyfield": "row1"},
        {"name": "test works!", "getbyfield": "row2"},
        {"name": "testing, so much fun .. yeah.", "getbyfield": "row3"},
    ]
    a.addMany(fixture)
    assert len(a.getAll()) == 3
    assert a.getByQuery({"getbyfield": "row1"})[0]["name"] == fixture[0]["name"]
    assert a.getByQuery({"getbyfield": "row2"})[0]["name"] == fixture[1]["name"]
    assert a.getByQuery({"getbyfield": "row3"})[0]["name"] == fixture[2]["name"]


def test_database_get_by_id(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(EMPTY_FIXTURE_STR)
    a = getDb(file.strpath)
    data = {"name": "test"}
    xactId = a.add(data)
    found = a.getById(xactId)
    assert len(found) == len(data)
    assert set(found.keys()) == set(data.keys())
    assert data['name'] == found['name']
    with pytest.raises(IdNotFoundError):
        a.getById(xactId+1)


def test_database_add_invalid_schema_exception(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(ID_FIXTURE_STR)
    a = getDb(file.strpath)
    with pytest.raises(SchemaError):
        a.add({"namme": "sd"})


def test_database_update(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(ID_FIXTURE_STR)
    a = getDb(file.strpath)
    a.updateByQuery({"name": "test"}, {"name": "test works!"})
    assert a.get()[0]["name"] == "test works!"
    with pytest.raises(DataNotFoundError):
        a.updateByQuery({"name": "test"}, {"name": "test works!"})
    with pytest.raises(SchemaError):
        a.updateByQuery({"naame": "test"}, {"namer": "test works!"})


def test_database_update_by_id(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(ID_FIXTURE_STR)
    a = getDb(file.strpath)
    a.updateById(ID_FIXTURE["data"][0]["id"], {"name": "test works!"})
    x = a.get()[0]["name"]
    assert a.get()[0]["name"] == "test works!"


def test_database_update_by_id_not_found(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(ID_FIXTURE_STR)
    a = getDb(file.strpath)
    with pytest.raises(IdNotFoundError):
        a.updateById(123, {"name": "not found :("})


def test_database_delete_by_id(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(ID_FIXTURE_STR)
    a = getDb(file.strpath)
    assert a.deleteById(ID_FIXTURE["data"][0]["id"])
    assert bool(len(a.get())) is True
    fixture = [
        {"name": "test", "getbyfield": "row1"},
        {"name": "test works!", "getbyfield": "row2"},
        {"name": "testing, so much fun .. yeah.", "getbyfield": "row3"},
    ]

    a.addMany(fixture)
    assert len(a.getAll()) == 3
    assert a.deleteById(a.get()[0]["id"])
    assert len(a.getAll()) == 2
    assert a.deleteById(a.get()[0]["id"])
    assert len(a.getAll()) == 1
    assert a.deleteById(a.get()[0]["id"])
    assert bool(len(a.get())) is True
    with pytest.raises(IdNotFoundError):
        assert a.deleteById(20)


def test_database_delete_all(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(ID_FIXTURE)
    a = getDb(file.strpath)
    assert a.deleteAll() is None


def test_database_research(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(EMPTY_FIXTURE_STR)
    a = getDb(file.strpath)
    fixture = [
        {"name": "test", "getbyfield": "row1"},
        {"name": "pysondb", "getbyfield": "row2"},
        {"name": "def23@c-py", "getbyfield": "row3"},
        {"name": "stuff(py", "getbyfield": "row4"}
    ]
    a.addMany(fixture)
    assert (a.reSearch("name", "test"))[0]["name"] == fixture[0]["name"]
    assert (a.reSearch("getbyfield", "row2"))[0]["getbyfield"] == fixture[1]["getbyfield"]
    assert (a.reSearch("name", r"\w{3}\d{2}@c-py"))[0]["name"] == fixture[2]["name"]
    assert (a.reSearch("name", r"stuff\(py"))[0]["name"] == fixture[3]["name"]
    