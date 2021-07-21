import os

import pytest

from pysondb import db


@pytest.fixture
def rm_file():
    yield
    os.remove("pysondb_test.json")


@pytest.fixture
def db_class():
    a = db.getDb("pysondb_test.json")
    yield a


@pytest.fixture
def db_w_data():
    """Database with data"""
    a = db.getDb("pysondb_test.json")
    a.addMany(
        [
            {"name": "ad", "age": 3},
            {"name": "fred", "age": 4},
            {"name": "test 1", "age": 5},
            {"name": "test 2", "age": 6},
        ]
    )
    yield a


@pytest.mark.usefixtures("rm_file")
def test_db_add(db_class):
    db_class.add({"name": "ad", "age": 3})
    assert len(db_class._db) == 1
    assert list(db_class._db.values()) == [{"name": "ad", "age": 3}]


@pytest.mark.usefixtures("rm_file")
def test_db_add_many(db_class):
    data = [{"name": "ad", "age": 3}, {"name": "fred", "age": 4}]
    db_class.addMany(data)
    assert len(db_class._db) == 2
    assert list(db_class._db.values()) == data


@pytest.mark.usefixtures("rm_file")
def test_db_get_all(db_w_data):
    assert list(db_w_data.getAll().values()) == [
        {"name": "ad", "age": 3},
        {"name": "fred", "age": 4},
        {"name": "test 1", "age": 5},
        {"name": "test 2", "age": 6},
    ]


@pytest.mark.usefixtures("rm_file")
def test_db_get_by(db_w_data):
    assert list(db_w_data.getBy({"name": "ad"}).values()) == [
        {"name": "ad", "age": 3}]
