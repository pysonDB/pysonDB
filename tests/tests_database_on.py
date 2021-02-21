import pytest

from pysondb.db import (Database, JsonDatabase, JsonUuidDatabase, YamlDatabase,
                        YamlUuidDatabase)


def test_notimplemented():
    with pytest.raises(NotImplementedError):
        Database().on("file.fantasyending")


def test_json_filending():
    db = Database().on("test.json")
    assert isinstance(db, JsonDatabase)


def test_json_filending_uuid():
    db = Database().on("test.json", uuid=True)
    assert isinstance(db, JsonUuidDatabase)


def test_yaml_filending():
    db = Database().on("test.yaml")
    assert isinstance(db, YamlDatabase)


def test_yaml_filending_uuid():
    db = Database().on("test.yaml", uuid=True)
    assert isinstance(db, YamlUuidDatabase)


def test_create():
    db = Database().on("test.yaml", uuid=True)
    assert isinstance(db, YamlUuidDatabase)
    db.add({"test": "hello"})


def test_create_false():
    db = Database().on("test_fail.yaml", uuid=True, create=False)
    assert isinstance(db, YamlUuidDatabase)
    with pytest.raises(FileNotFoundError):
        db.add({"test": "hello"})
