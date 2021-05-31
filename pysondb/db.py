import json
import logging
import os
import re
import uuid
from pathlib import Path

import yaml
from filelock import FileLock

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pysondb")


class DataNotFoundError(Exception):
    """Exception raised if id not found.

    Attributes:
        data
    """

    def __init__(self, data):
        self.data = data


class IdNotFoundError(Exception):
    """Exception raised if id not found.

    Attributes:
        pk -- primary key / id
    """

    def __init__(self, pk):
        self.pk = pk


class SchemaError(Exception):
    """Exception raised for field/key errors."""

    def __init__(self, *args):
        self.args = args


class JsonDatabase:
    def __init__(self, filename, id_fieldname="id"):
        a = Database().on(filename)
        sdx = Path(filename)
        self._id_fieldname = id_fieldname
        logger.info("Database Filename: {0}".format(sdx))
        self.filename = filename
        self.lock = FileLock("{}.lock".format(self.filename))

    def _get_id(self):
        return int(str(uuid.uuid4().int)[:18])

    def _cast_id(self, pk):
        return int(pk)

    def _get_load_function(self):
        return json.load

    def _get_dump_function(self):
        return json.dump

    @property
    def id_fieldname(self):
        return self._id_fieldname

    def add(self, new_data):
        with self.lock:
            with open(self.filename, "r+") as db_file:
                db_data = self._get_load_function()(db_file)
                try:
                    if set(db_data["data"][0].keys()) == set(new_data.keys()).union(
                        [self.id_fieldname]
                    ):
                        new_data[self.id_fieldname] = self._get_id()
                        logger.debug("Append new data; {0}".format(new_data))
                        db_data["data"].append(new_data)
                        db_file.seek(0)
                        self._get_dump_function()(db_data, db_file)
                        return new_data[self.id_fieldname]
                    else:
                        raise SchemaError(
                            "db_keys: "
                            + ",".join(sorted(list(db_data["data"][0].keys()))),
                            "new_data_keys: "
                            + ",".join(
                                sorted(list(new_data.keys()) + [self.id_fieldname])
                            ),
                        )
                except IndexError:
                    new_data[self.id_fieldname] = self._get_id()
                    db_data["data"].append(new_data)
                    logger.debug("Add first data entry; {0}".format(new_data))
                    db_file.seek(0)
                    self._get_dump_function()(db_data, db_file)
                return new_data[self.id_fieldname]

    def addMany(self, new_data):
        with self.lock:
            with open(self.filename, "r+") as db_file:
                db_data = self._get_load_function()(db_file)
                try:
                    for d in new_data:
                        if set(db_data["data"][0].keys()) == set(d.keys()).union(
                            [self.id_fieldname]
                        ):
                            d[self.id_fieldname] = self._get_id()
                            db_data["data"].append(d)
                            db_file.seek(0)
                            self._get_dump_function()(db_data, db_file)
                except:
                    keys = list(new_data[0].keys())
                    for d in new_data:
                        if set(keys) == set(d.keys()):
                            d[self.id_fieldname] = self._get_id()
                            db_data["data"].append(d)
                            db_file.seek(0)
                            self._get_dump_function()(db_data, db_file)

    def getAll(self):
        with self.lock:
            with open(self.filename, "r", encoding="utf8") as db_file:
                db_data = self._get_load_function()(db_file)
            return db_data["data"]

    def get(self, num=1):
        with self.lock:
            try:
                with open(self.filename, "r", encoding="utf8") as db_file:
                    db_data = self._get_load_function()(db_file)
                if num <= len(db_data["data"]):
                    return db_data["data"][0 : int(num)]
                else:
                    logger.info(
                        "The length you have given {} \n Length of the database items= {}".format(
                            num, len(db_data["data"])
                        )
                    )
                    return []
            except:
                return []

    def getBy(self, query):
        with self.lock:
            result = []
            with open(self.filename, "r") as db_file:
                db_data = self._get_load_function()(db_file)
                for d in db_data["data"]:
                    if all(x in d and d[x] == query[x] for x in query):
                        result.append(d)
            return result

    def reSearch(self, key, _re):
        pattern = _re
        if not isinstance(_re, re.Pattern):
            pattern = re.compile(str(_re))

        items = []
        data = self.getAll()

        for d in data:
            for k in d.keys():
                if re.match(pattern, str(d[k])) and k == key:
                    items.append(d)
                    continue

        return items

    def updateById(self, pk, new_data):
        with self.lock:
            with open(self.filename, "r+") as db_file:
                db_data = self._get_load_function()(db_file)
                result = []
                if set(new_data.keys()).issubset(db_data["data"][0].keys()):
                    for d in db_data["data"]:
                        if d[self.id_fieldname] == self._cast_id(pk):
                            d.update(new_data)
                            result.append(d)
                        else:
                            raise IdNotFoundError(pk)
                    db_data["data"] = result
                    db_file.seek(0)
                    db_file.truncate()
                    self._get_dump_function()(db_data, db_file)
                else:
                    raise SchemaError(
                        "db_keys: " + ",".join(sorted(db_data.keys())),
                        "new_keys: " + ",".join(sorted(new_data.keys())),
                    )

    def deleteById(self, pk):
        with self.lock:
            with open(self.filename, "r+") as db_file:
                db_data = self._get_load_function()(db_file)
                result = []
                found = False

                for d in db_data["data"]:
                    if d[self.id_fieldname] == self._cast_id(pk):
                        found = True
                    else:
                        result.append(d)

                if not found:
                    raise IdNotFoundError(pk)

                db_data["data"] = result
                db_file.seek(0)
                db_file.truncate()
                self._get_dump_function()(db_data, db_file)
            return True

    def update(self, db_dataset, new_dataset):
        with self.lock:
            with open(self.filename, "r+") as db_file:
                db_data = self._get_load_function()(db_file)
                result = []
                found = False
                if set(db_dataset.keys()).issubset(db_data["data"][0].keys()) and set(
                    new_dataset.keys()
                ).issubset(db_data["data"][0].keys()):
                    for d in db_data["data"]:
                        if all(x in d and d[x] == db_dataset[x] for x in db_dataset):
                            if set(new_dataset.keys()).issubset(
                                db_data["data"][0].keys()
                            ):
                                d.update(new_dataset)
                                result.append(d)
                                found = True
                        else:
                            result.append(d)

                    if not found:
                        raise DataNotFoundError(db_dataset)

                    db_data["data"] = result
                    db_file.seek(0)
                    db_file.truncate()
                    self._get_dump_function()(db_data, db_file)
                else:
                    raise SchemaError(
                        "db_dataset_keys: " + ",".join(sorted(list(db_dataset.keys()))),
                        "db_keys: " + ",".join(sorted(list(db_data["data"][0].keys()))),
                        "new_dataset_keys: "
                        + ",".join(sorted(list(new_dataset.keys()))),
                    )


class UuidDatabase(JsonDatabase):
    def _get_id(self):
        return str(uuid.uuid4())

    def _cast_id(self, pk):
        return pk


class YamlDatabase(JsonDatabase):
    def _get_load_function(self):
        return yaml.safe_load

    def _get_dump_function(self):
        return yaml.dump


class JsonUuidDatabase(UuidDatabase):
    pass


class YamlUuidDatabase(UuidDatabase, YamlDatabase):
    pass


EMPTY_DATA = {"data": []}


class Database:
    def create(self, filename, data):
        with open(filename, "w") as db_file:
            db_file.write(data)

    def on(self, filename, uuid=True, create=True):
        if filename.split(".")[-1:][0] == "json":
            if create and not os.path.exists(filename):
                self.create(filename, json.dumps(EMPTY_DATA))


getDb = JsonDatabase  # for legacy support.
