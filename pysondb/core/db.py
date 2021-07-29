import json
import re
from pathlib import Path
from pprint import pformat
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Pattern
from typing import Union

from .errors import DataError
from .utils import create_db
from .utils import get_id
from .utils import verify_data

# current DB design
# {3498634873847: {"name": "ad", "age": "test"}}


# the JSON DB
class JsonDatabase:
    def __init__(self, filename: str) -> None:
        create_db(filename)  # create the JSON file if it doesn't exists

        self._db: Dict[str, Dict[str, Any]]

        self.filename = filename

        # load the existing DB to the in memory copy
        self._load_db_from_file()

    def __repr__(self) -> str:
        return pformat(self._db, sort_dicts=False, width=80)

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

    def add(self, data: Dict[str, Any]) -> str:
        """Add the gives data to the DB"""

        if verify_data(data, self._db):
            _id = get_id(self._db)
            print(type(_id))

            self._db[_id] = data

            self._dump_db_to_file()
            return _id

        return ""

    def addMany(self, new_data: List[Dict[str, Any]]) -> None:
        """Adds a list of values to the DB"""

        # if any of the data in the list is invalid, prevents all the other data in the list
        # from entering the DB
        db_clone = self._db.copy()

        # schema verification
        # steps 1) verify the first entry with the DB
        # 2) verify all the other entries with the first entry

        verified_data: Dict[str, Any] = {}

        if verify_data(new_data[0], db_clone):
            verified_data = new_data[0]

        for d in new_data:
            if all(i in d.keys() for i in verified_data.keys()) and len(d) == len(verified_data):
                db_clone[get_id(db_clone)] = d
            else:
                raise DataError(
                    "The Data provided does not comply with the schema")

        self._db = db_clone.copy()
        del [db_clone]
        self._dump_db_to_file()

    def getAll(self) -> Dict[str, Dict[str, Any]]:
        """Returns the entire DB"""

        return self._db.copy()

    def get(self, key: str) -> Union[None, Dict[str, Any]]:
        """Returns the DB values based on their id"""

        if key in self._db:
            return self._db[key]

        return None

    def getBy(self, query: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """Returns the DB values based on the condition in the query"""
        return {
            i: x
            for i, x in self._db.items()
            if all(k in x and x[k] == v for k, v in query.items())
        }

    def reSearch(
        self, key: str, _re: Union[str, Pattern[str]]
    ) -> List[Dict[str, Dict[str, Any]]]:
        """Returns the DB values based on the regex pattern of the key provided"""

        pattern = _re
        if not isinstance(_re, re.Pattern):
            pattern = re.compile(str(_re))

        items = []

        for k, d in self._db.items():
            if key in d:
                if re.match(pattern, str(d[key])):
                    items.append({k: d})
            else:
                raise KeyError(f"The key {key} does not exist in DB")

        return items

    def updateById(self, pk: str, new_data: Dict[str, Any]) -> None:

        if self._db:
            if all(i in list(self._db.values())[0] for i in new_data):
                if pk in self._db:
                    self._db[pk].update(new_data)

                    self._dump_db_to_file()

            else:
                raise KeyError(
                    "Some keys provided in the update data does not match the keys in the DB"
                )

    def updateBy(self, query: Dict[str, Any], new_data: Dict[str, Any]) -> None:

        if self._db:
            if all(i in list(self._db.values())[0] for i in query) and all(
                i in list(self._db.values())[0] for i in new_data
            ):
                ids = list(
                    self.getBy(query)
                )  # get the ids of all the values that need to updated
                for i in ids:
                    self.updateById(i, new_data)  # update each of them

                self._dump_db_to_file()

            else:
                raise KeyError(
                    "The key in the query or the key in the new_data does not match the keys in the DB"
                )

    def deleteById(self, pk: str) -> None:
        if pk in self._db:
            del self._db[pk]
            self._dump_db_to_file()

    def deleteAll(self) -> None:
        self._db.clear()
        self._dump_db_to_file()


getDb = JsonDatabase  # for legacy support.
