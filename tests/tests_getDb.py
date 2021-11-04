import pytest

from pysondb.db import (getDb, JsonDatabase)


def test_json_filending(tmpdir):
    file = tmpdir.join("test.json")
    db = getDb(file.strpath)
    assert isinstance(db, JsonDatabase)
    