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
