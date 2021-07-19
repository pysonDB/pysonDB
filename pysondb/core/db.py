import json
import os
import re
from pathlib import Path
from pprint import pformat
from typing import Any, Callable, Dict, List, Union

from .errors import DataError, DataNotFoundError, IdNotFoundError, SchemaError
from .utils import create_db, get_id, verify_data

# current DB design
# {3498634873847: {"name": "ad", "age": "test"}}


# util functions


# the JSON DB


class JsonDatabase:
    def __init__(self, filename: str) -> None:
        create_db(filename)  # create the JSON file if it doesn't exists

        self._db: Dict[int, Dict[str, Any]]

        self.filename = filename

        # load the existing DB to the in memory copy
        self._load_db_from_file()

    def __repr__(self) -> str:
        return pformat(self._db, sort_dicts=False, width=80)

    def _cast_id(self, pk) -> int:
        return int(pk)

    def _get_load_function(self) -> Callable[..., Any]:
        return json.load

    def _get_dump_function(self) -> Callable[..., Any]:
        return json.dump

    def _load_db_from_file(self) -> None:
        """Loads the DB if the file exists"""

        if self.filename.endswith(".json") and Path(self.filename).is_file() is True:
            with open(self.filename, "r", encoding="utf-8") as f:
                self._db = self._get_load_function()(f)

    def _dump_db_to_file(self) -> None:
        """Dump the current isinstance of the DB to the .json file"""
        with open(self.filename, "w", encoding="utf-8") as f:
            self._get_dump_function()(self._db, f, indent=4)

    def add(self, data: Dict[str, Any]) -> int:
        if verify_data(data, self._db):
            _id = get_id(self._db)
            self._db[_id] = data

            self._dump_db_to_file()
            return _id

        return 0

    def addMany(self, new_data: List[Dict[str, Any]]) -> None:

        # if any of the data in the list is invalid, prevents all the other data in the list
        # from entering the DB
        db_clone = self._db.copy()

        for d in new_data:
            if verify_data(d, db_clone):
                _id = get_id(db_clone)
                db_clone[_id] = d

        self._db = db_clone.copy()
        del [db_clone]
        self._dump_db_to_file()

    def getAll(self) -> Dict[int, Dict[str, Any]]:
        return self._db

    def get(self, key: int) -> Union[None, Dict[str, Any]]:
        if key in self._db:
            return self._db[key]

        return None

    def getBy(self, query: Dict[str, Any]) -> None:
        pass

    def reSearch(self, key: str, _re: Union[str, re.Pattern]) -> List[Dict[str, Any]]:

        pattern = _re
        if not isinstance(_re, re.Pattern):
            pattern = re.compile(str(_re))

        items = []

        for d in self._db.values():
            if key in d:
                if re.match(pattern, str(d[key])):
                    items.append(d)
            else:
                raise KeyError(f"The key {key} does not exist in DB")

        return items

    def updateById(self, pk: int, new_data: Dict[str, Any]) -> None:

        if verify_data(new_data):
            if pk in self._db:
                self._db[pk] = new_data

                self._dump_db_to_file()

    def deleteById(self, pk: int) -> bool:
        if pk in self._db:
            del self._db[pk]
            self._dump_db_to_file()

    def deleteAll(self) -> None:
        self._db.clear()
        self._dump_db_to_file()

    # def update(self, db_dataset: Dict[str, Any], new_dataset: Dict[str, Any]) -> None:
    #     with self.lock:
    #         with open(self.filename, "r+") as db_file:
    #             db_data = self._get_load_function()(db_file)
    #             result = []
    #             found = False
    #             if set(db_dataset.keys()).issubset(db_data["data"][0].keys()) and set(
    #                 new_dataset.keys()
    #             ).issubset(db_data["data"][0].keys()):
    #                 for d in db_data["data"]:
    #                     if all(x in d and d[x] == db_dataset[x] for x in db_dataset):
    #                         if set(new_dataset.keys()).issubset(
    #                             db_data["data"][0].keys()
    #                         ):
    #                             d.update(new_dataset)
    #                             result.append(d)
    #                             found = True
    #                     else:
    #                         result.append(d)

    #                 if not found:
    #                     raise DataNotFoundError(db_dataset)

    #                 db_data["data"] = result
    #                 db_file.seek(0)
    #                 db_file.truncate()
    #                 self._get_dump_function()(db_data, db_file, indent=3)
    #             else:
    #                 raise SchemaError(
    #                     "db_dataset_keys: " + ",".join(sorted(list(db_dataset.keys()))),
    #                     "db_keys: " + ",".join(sorted(list(db_data["data"][0].keys()))),
    #                     "new_dataset_keys: "
    #                     + ",".join(sorted(list(new_dataset.keys()))),
    #                 )


getDb = JsonDatabase  # for legacy support.
