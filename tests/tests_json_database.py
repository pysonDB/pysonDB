import json
import uuid

import pytest

from pysondb.db import (Database, DataNotFoundError, IdNotFoundError,
                        SchemaError, UuidDatabase)

ID_FIXTURE = {"data": [{"id": 9999999999, "name": "test"}]}
ID_FIXTURE_STR = json.dumps(ID_FIXTURE)
EMPTY_FIXTURE_STR = json.dumps({"data": []})


def test_database_add(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(EMPTY_FIXTURE_STR)
    db = Database().on(file.strpath, uuid=False)
    x = db.add({"name": "test"})
    assert int(x)


def test_database_add_many(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(EMPTY_FIXTURE_STR)
    db = Database().on(file.strpath, uuid=False)
    db.addMany([{"name": "test"}, {"name": "test2"}])
    data = db.getAll()
    assert len(data) == 2
    for d in data:
        assert int(d["id"])


def test_database_get(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(EMPTY_FIXTURE_STR)
    db = Database().on(file.strpath, uuid=False)
    fixture = [
        {"name": "test", "getbyfield": "row1"},
        {"name": "test works!", "getbyfield": "row2"},
        {"name": "testing, so much fun .. yeah.", "getbyfield": "row3"},
    ]
    db.addMany(fixture)
    assert len(db.get(1)) == 1
    assert len(db.get(2)) == 2
    assert len(db.get(3)) == 3


def test_database_get_by(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(EMPTY_FIXTURE_STR)
    db = Database().on(file.strpath, uuid=False)
    fixture = [
        {"name": "test", "getbyfield": "row1"},
        {"name": "test works!", "getbyfield": "row2"},
        {"name": "testing, so much fun .. yeah.", "getbyfield": "row3"},
    ]
    db.addMany(fixture)
    assert len(db.getAll()) == 3
    assert db.getBy({"getbyfield": "row1"})[0]["name"] == fixture[0]["name"]
    assert db.getBy({"getbyfield": "row2"})[0]["name"] == fixture[1]["name"]
    assert db.getBy({"getbyfield": "row3"})[0]["name"] == fixture[2]["name"]


def test_database_get_by_id(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(EMPTY_FIXTURE_STR)
    db = Database().on(file.strpath, uuid=False)
    data = {"name": "test"}
    xactId = db.add(data)
    found = db.getById(xactId)
    assert len(found) == len(data)
    assert set(found.keys()) == set(data.keys())
    for k in data.keys:
        assert data[k] == found[k]
    with pytest.raises(IdNotFoundError):
        db.getById(xactId+1)


def test_database_add_invalid_schema_exception(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(ID_FIXTURE_STR)
    db = Database().on(file.strpath, uuid=False)
    with pytest.raises(SchemaError):
        db.add({"namme": "sd"})


def test_database_update(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(ID_FIXTURE_STR)
    db = Database().on(file.strpath, uuid=False)
    db.update({"name": "test"}, {"name": "test works!"})
    assert db.get()[0]["name"] == "test works!"
    with pytest.raises(DataNotFoundError):
        db.update({"name": "test"}, {"name": "test works!"})
    with pytest.raises(SchemaError):
        db.update({"naame": "test"}, {"namer": "test works!"})


def test_database_update_by_id(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(ID_FIXTURE_STR)
    db = Database().on(file.strpath, uuid=False)
    db.updateById(ID_FIXTURE["data"][0]["id"], {"name": "test works!"})
    x = db.get()[0]["name"]
    assert db.get()[0]["name"] == "test works!"


def test_database_update_by_id_not_found(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(ID_FIXTURE_STR)
    db = Database().on(file.strpath, uuid=False)
    with pytest.raises(IdNotFoundError):
        db.updateById(123, {"name": "not found :("})


def test_database_delete_by_id(tmpdir):
    file = tmpdir.join("test.db.json")
    file.write(ID_FIXTURE_STR)
    db = Database().on(file.strpath, uuid=False)
    assert db.deleteById(ID_FIXTURE["data"][0]["id"])
    assert not bool(len(db.get()))
    fixture = [
        {"name": "test", "getbyfield": "row1"},
        {"name": "test works!", "getbyfield": "row2"},
        {"name": "testing, so much fun .. yeah.", "getbyfield": "row3"},
    ]
    db.addMany(fixture)
    assert len(db.getAll()) == 3
    assert db.deleteById(db.get()[0]["id"])
    assert len(db.getAll()) == 2
    assert db.deleteById(db.get()[0]["id"])
    assert len(db.getAll()) == 1
    assert db.deleteById(db.get()[0]["id"])
    assert not bool(len(db.get()))
    with pytest.raises(IdNotFoundError):
        assert db.deleteById(20)
