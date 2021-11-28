import os
import csv
import pytest

from pysondb.db import getDb
from pysondb.cli import set_parser


def tests_create(tmpdir, capsys):
    file = tmpdir.join("test.db.json")
    set_parser(['create', file.strpath])
    out, err = capsys.readouterr()
    assert out == f"Successfully created {file.strpath} in the directory.\n"
    assert err == ''

def tests_show(tmpdir):
    json_file = tmpdir.join('test.json')
    a = getDb(json_file.strpath)
    json_data = [{"name": "test1"}, {"name": "test2"}]
    a.addMany(json_data)
    out = set_parser(['show', json_file.strpath])
    assert out == 0

def tests_delete_empty_string(tmpdir, capsys):
    set_parser(['delete', ''])
    out, err = capsys.readouterr()
    assert out == 'The file does not exist\n'

def tests_merge(tmpdir, capsys):
    file1 = tmpdir.join("test1.json")
    set_parser(['create', file1.strpath])
    a1 = getDb(file1.strpath)
    data1  = {"name": "test1"}
    a1.add(data1)

    file2 = tmpdir.join("test2.json")
    set_parser(['create', file2.strpath])
    a2 = getDb(file2.strpath)
    data2 = {"name": "test2"}
    a2.add(data2)

    out = set_parser(['merge', file1.strpath, file2.strpath])
    assert out == 0

def tests_convert(tmpdir):
    csv_file = tmpdir.join('test.csv')
    fields = ['name', 'type']
    rows = [['test', 'cli']]
    with open(csv_file, 'w') as csvfile:
        csvwriter  = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    json_file = tmpdir.join('test.json')
    out = set_parser(['convert', csv_file.strpath, json_file.strpath])
    assert out == 0

def tests_convert_db_to_csv(tmpdir):
    json_file = tmpdir.join('test.json')
    a = getDb(json_file.strpath)
    json_data = [{"name": "test1"}, {"name": "test2"}]
    a.addMany(json_data)

    csv_file = tmpdir.join('test.csv')
    out = set_parser(['converttocsv', json_file.strpath, '-t', csv_file.strpath])
    assert out == 0
    