import json
import uuid

import pytest
import yaml

from pysondb.db import (Database, DataNotFoundError, IdNotFoundError,
                        SchemaError)

EMPTY_FIXTURE_STR = yaml.dump({"data": []})
UUID_FIXTURE = {
    "data": [{"id": "b337ec3c-c03d-46c4-bfe5-70a17f1c03a0", "name": "test"}]
}
UUID_FIXTURE_STR = yaml.dump(UUID_FIXTURE)


def test_database_add(tmpdir):
    file = tmpdir.join("test.db.yaml")
    file.write(EMPTY_FIXTURE_STR)
    db = Database().on(file.strpath)
    x = db.add({"name": "test"})
    assert uuid.UUID(x)


def test_database_add_many(tmpdir):
    file = tmpdir.join("test.db.yaml")
    file.write(EMPTY_FIXTURE_STR)
    db = Database().on(file.strpath)
    db.addMany([{"name": "test"}, {"name": "test2"}])
    data = db.getAll()
    assert len(data) == 2
    for d in data:
        assert uuid.UUID(d["id"])


def test_database_get(tmpdir):
    file = tmpdir.join("test.db.yaml")
    file.write(EMPTY_FIXTURE_STR)
    db = Database().on(file.strpath)
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
    file = tmpdir.join("test.db.yaml")
    file.write(EMPTY_FIXTURE_STR)
    db = Database().on(file.strpath)
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
    file = tmpdir.join("test.db.yaml")
    file.write(EMPTY_FIXTURE_STR)
    db = Database().on(file.strpath)
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
    file = tmpdir.join("test.db.yaml")
    file.write(UUID_FIXTURE_STR)
    db = Database().on(file.strpath)
    with pytest.raises(SchemaError):
        db.add({"namme": "sd"})


def test_database_update(tmpdir):
    file = tmpdir.join("test.db.yaml")
    file.write(UUID_FIXTURE_STR)
    db = Database().on(file.strpath)
    db.update({"name": "test"}, {"name": "test works!"})
    assert db.get()[0]["name"] == "test works!"
    with pytest.raises(DataNotFoundError):
        db.update({"name": "test"}, {"name": "test works!"})
    with pytest.raises(SchemaError):
        db.update({"naame": "test"}, {"namer": "test works!"})


def test_database_update_by_id(tmpdir):
    file = tmpdir.join("test.db.yaml")
    file.write(UUID_FIXTURE_STR)
    db = Database().on(file.strpath)
    db.updateById(UUID_FIXTURE["data"][0]["id"], {"name": "test works!"})
    x = db.get()[0]["name"]
    assert db.get()[0]["name"] == "test works!"


def test_database_update_by_id_not_found(tmpdir):
    file = tmpdir.join("test.db.yaml")
    file.write(UUID_FIXTURE_STR)
    db = Database().on(file.strpath)
    with pytest.raises(IdNotFoundError):
        db.updateById(123, {"name": "not found :("})


def test_database_delete_by_id(tmpdir):
    file = tmpdir.join("test.db.yaml")
    file.write(UUID_FIXTURE_STR)
    db = Database().on(file.strpath)
    assert db.deleteById(UUID_FIXTURE["data"][0]["id"])
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
