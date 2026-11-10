"""Regression tests: `show` must report bad inputs cleanly, not traceback."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pysondb.cli import show


def _write(tmp_path, name, content):
    target = tmp_path / name
    target.write_text(content, encoding="utf-8")
    return str(target)


def test_show_missing_file(capsys, tmp_path):
    assert show(str(tmp_path / "nope.json")) == 1
    assert "does not exist" in capsys.readouterr().out


def test_show_malformed_json(capsys, tmp_path):
    path = _write(tmp_path, "bad.json", "{not json")
    assert show(path) == 1
    assert "not a valid database file" in capsys.readouterr().out


def test_show_missing_data_key(capsys, tmp_path):
    path = _write(tmp_path, "nodata.json", json.dumps({"other": []}))
    assert show(path) == 1
    assert "not a valid database file" in capsys.readouterr().out


def test_show_non_list_data(capsys, tmp_path):
    path = _write(tmp_path, "shape.json", json.dumps({"data": {"a": 1}}))
    assert show(path) == 1
    assert "not a valid database file" in capsys.readouterr().out


def test_show_empty_database(capsys, tmp_path):
    path = _write(tmp_path, "empty.json", json.dumps({"data": []}))
    assert show(path) == 1
    assert "Database is empty." in capsys.readouterr().out


def test_show_valid_database(capsys, tmp_path):
    path = _write(
        tmp_path, "db.json", json.dumps({"data": [{"id": 1, "task": "milk"}]})
    )
    assert show(path) == 0
    assert "milk" in capsys.readouterr().out
