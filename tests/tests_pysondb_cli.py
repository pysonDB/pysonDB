import os
import csv
import pytest

from pysondb.db import getDb
from pysondb.cli import (create_if_not_exist, delete, merge, convert, convert_db_to_csv)


def tests_create_if_not_exist(tmpdir):
    file = tmpdir.join("test.db.json")
    create_if_not_exist(file)
    a = getDb(file.strpath)
    a.add({"name": "test"})
    data = a.get()
    assert bool(os.path.exists(file)) is True
    assert data[0]["name"] == "test"

def tests_delete(tmpdir):
    file = tmpdir.join("test.db.json")
    delete(file)
    assert bool(os.path.exists(file)) is False

def tests_merge(tmpdir):
    file1 = tmpdir.join("test1.json")
    create_if_not_exist(file1)
    a1 = getDb(file1.strpath)
    data1  = {"name": "test1"}
    a1.add(data1)

    file2 = tmpdir.join("test2.json")
    create_if_not_exist(file2)
    a2 = getDb(file2.strpath)
    data2 = {"name": "test2"}
    a2.add(data2)

    merge(file1, file2, 'merge.json')
    output_file = getDb('merge.json')
    data = output_file.getAll()
    assert data[0]["name"] == data2["name"]
    assert data[1]["name"] == data1["name"]

def tests_convert(tmpdir):
    csv_file = tmpdir.join('test.csv')
    fields = ['name', 'type']
    rows = [['test', 'cli']]
    with open(csv_file, 'w') as csvfile:
        csvwriter  = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    json_file = tmpdir.join('test.json')
    convert(csv_file, json_file)
    a = getDb(json_file.strpath)
    data = a.get()
    assert data[0]["name"] == rows[0][0]
    assert data[0]["type"] == rows[0][1]

def tests_convert_db_to_csv(tmpdir):
    json_file = tmpdir.join('test.json')
    a = getDb(json_file.strpath)
    json_data = [{"name": "test1"}, {"name": "test2"}]
    a.addMany(json_data)
    data = a.getAll()

    csv_file = tmpdir.join('test.csv')
    convert_db_to_csv(json_file, csv_file)

    rows = []
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)

    assert data[0]["name"] == rows[1][0]
    assert data[1]["name"] == rows[2][0]