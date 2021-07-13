import json
import logging
import os
import re
import uuid
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Callable, Dict, List, Union

from filelock import FileLock

# consants
EMPTY_DATA: Dict[str, Any] = {"data": []}

# types
getType = Union[List[Dict[str, Any]], List[SimpleNamespace]]

# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pysondb")
logger.setLevel(logging.DEBUG)

# Errors
class DataNotFoundError(Exception):
    """Exception raised if id not found.

    Attributes:
        data
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        self.data = data

    def __str__(self) -> str:
        return f"The data {self.data!r} does not exists in JSON db"


class IdNotFoundError(Exception):
    """Exception raised if id not found.

    Attributes:
        pk -- primary key / id
    """

    def __init__(self, pk: int) -> None:
        self.pk = pk

    def __str__(self) -> str:
        return f"Id {self.pk!r} does not exist in the JSON db"


class SchemaError(Exception):
    """Exception raised for field/key errors."""

    def __init__(self, *args) -> None:
        self.args = args

    def __str__(self) -> str:
        return str(self.args)


# util functions
def create_db(filename: str, create_file: bool = True) -> True:
    def create(filename: str, data: str) -> None:
        with open(filename, "w") as db_file:
            db_file.write(data)

    if filename.endswith(".json"):
        if create_file and not os.path.exists(filename):
            create(filename, json.dumps(EMPTY_DATA))


# the JSON DB


class JsonDatabase:
    def __init__(
        self, filename: str, id_fieldname: str = "id", log: bool = False
    ) -> None:
        create_db(filename)  # create the JSON file if it doesn't exists
        sdx = Path(filename)

        self._id_fieldname = id_fieldname
        self.filename = filename
        self.lock = FileLock("{}.lock".format(self.filename))

        if not log:
            self._stop_log()

        logger.info("Database Filename: {0}".format(sdx))

    def _get_id(self) -> int:
        return int(str(uuid.uuid4().int)[:18])

    def _cast_id(self, pk) -> int:
        return int(pk)

    def _get_load_function(self) -> Callable[..., Any]:
        return json.load

    def _get_dump_function(self) -> Callable[..., Any]:
        return json.dump

    @staticmethod
    def _objectify(data) -> SimpleNamespace:
        return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

    @staticmethod
    def _stop_log() -> None:
        logging.getLogger("pysondb").disabled = True
        logging.getLogger("filelock").disabled = True

    @property
    def id_fieldname(self) -> str:
        return self._id_fieldname

    def add(self, new_data: Dict[str, Any]) -> int:
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
                        self._get_dump_function()(db_data, db_file,indent=3)
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
                    self._get_dump_function()(db_data, db_file,indent=3)
                return new_data[self.id_fieldname]

    def addMany(self, new_data: List[Dict[str, Any]]) -> None:
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
                            self._get_dump_function()(db_data, db_file,indent=3)
                except:
                    keys = list(new_data[0].keys())
                    for d in new_data:
                        if set(keys) == set(d.keys()):
                            d[self.id_fieldname] = self._get_id()
                            db_data["data"].append(d)
                            db_file.seek(0)
                            self._get_dump_function()(db_data, db_file,indent=3)

    def getAll(self, objectify=False) -> getType:
        with self.lock:
            with open(self.filename, "r", encoding="utf8") as db_file:
                db_data = self._get_load_function()(db_file)

            return (
                db_data["data"]
                if not objectify
                else self._objectify(json.dumps(db_data)).data
            )

    def get(self, num: int = 1, objectify: bool = False) -> getType:
        with self.lock:
            try:
                with open(self.filename, "r", encoding="utf8") as db_file:
                    db_data = self._get_load_function()(db_file)
                if num <= len(db_data["data"]):
                    data = db_data["data"][0 : int(num)]
                    return (
                        data
                        if not objectify
                        else self._objectify(json.dumps({"data": data})).data
                    )
                else:
                    logger.info(
                        "The length you have given {} \n Length of the database items= {}".format(
                            num, len(db_data["data"])
                        )
                    )
                    return [{"": ""}]
            except:
                return [{"": ""}]

    def getBy(self, query: Dict[str, Any], objectify: bool = False) -> getType:
        with self.lock:
            result = []
            with open(self.filename, "r") as db_file:
                db_data = self._get_load_function()(db_file)
                for d in db_data["data"]:
                    if all(x in d and d[x] == query[x] for x in query):
                        result.append(d)
            return (
                result
                if not objectify
                else self._objectify(json.dumps({"data": result})).data
            )

    def reSearch(
        self, key: str, _re: Union[str, re.Pattern], objectify: bool = False
    ) -> getType:

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

        return (
            items
            if not objectify
            else self._objectify(json.dumps({"data": items})).data
        )

    def updateById(self, pk: int, new_data: Dict[str, Any]) -> None:
        updated = False

        with self.lock:
            with open(self.filename, "r+") as db_file:
                db_data = self._get_load_function()(db_file)
                result = []
                if set(new_data.keys()).issubset(db_data["data"][0].keys()):
                    for d in db_data["data"]:
                        if d[self.id_fieldname] == self._cast_id(pk):
                            d.update(new_data)
                            updated = True

                        result.append(d)

                    else:
                        if not updated:
                            raise IdNotFoundError(pk)
                    db_data["data"] = result
                    db_file.seek(0)
                    db_file.truncate()
                    self._get_dump_function()(db_data, db_file,indent=3)
                else:
                    raise SchemaError(
                        "db_keys: " + ",".join(sorted(db_data.keys())),
                        "new_keys: " + ",".join(sorted(new_data.keys())),
                    )

    def deleteById(self, pk: int) -> bool:
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
   
    def deleteAll(self) -> None:
        with self.lock:
            with open(self.filename, "w") as f:
                f.write(json.dumps(EMPTY_DATA))

    def update(self, db_dataset: Dict[str, Any], new_dataset: Dict[str, Any]) -> None:
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
                    self._get_dump_function()(db_data, db_file,indent=3)
                else:
                    raise SchemaError(
                        "db_dataset_keys: " + ",".join(sorted(list(db_dataset.keys()))),
                        "db_keys: " + ",".join(sorted(list(db_data["data"][0].keys()))),
                        "new_dataset_keys: "
                        + ",".join(sorted(list(new_dataset.keys()))),
                    )


    def updateArray(self, query, prop, value, capacity=float('inf')):
        with self.lock:
            with open(self.filename, "r+") as db_file:
                db_data = self._get_load_function()(db_file)
                for d in db_data["data"]:
                    if all(x in d and d[x] == query[x] for x in query):
                        try:
                            if isinstance(d[prop], list):
                                if len(d[prop]) < capacity:
                                    d[prop].append(value)
                                else:
                                    d[prop].pop(0)
                                    d[prop].append(value)
                            else:
                                raise TypeError(
                                    " property '" + prop + "' is not an array."
                                )
                        except KeyError:
                            raise SchemaError(
                                " the queried object has no attribute '"+prop+"'"
                            )
                db_file.seek(0)
                self._get_dump_function()(db_data, db_file)



getDb = JsonDatabase  # for legacy support.
