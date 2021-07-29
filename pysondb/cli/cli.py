import csv
import json
import os
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import fire
from beautifultable import BeautifulTable

from pysondb.core.db import getDb


def create_if_not_exist(file_name: str) -> None:
    """
    Checks for the existence of the provided JSON DB.
    If it does not, this will add {data:[]}.
    :param str file_name: The absolute path to the DB file
    """
    if not os.path.exists(file_name):
        with open(file_name, "w") as db_file:
            db: Dict[str, Any] = {}
            json.dump(db, db_file)
        print("Succesfully created {} in the directory.".format(file_name))


def display(file_name: str) -> None:

    if file_name.endswith(".json") and Path(file_name).is_file() is True:

        table = BeautifulTable()
        with open(file_name) as jsondoc:
            data = json.load(jsondoc)
            if data:
                header = ["id"] + list(list(data.values())[0].keys())
                for _id, data in data.items():
                    table.rows.append([_id] + list(data.values()))
                table.columns.header = header
                print(table)


def delete(file_name: str) -> None:
    if Path(file_name).is_file() is True and file_name.endswith(".json"):
        x = input("Do you want to remove the json file..(y/n)")
        if x.lower() == "y":
            os.remove(file_name)
        else:
            print("Action terminated")
    else:
        print("The file does not exist")


def convert(csv_file: str, json_db: str) -> None:
    if csv_file.endswith(".csv") and Path(csv_file).is_file() is True:
        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)

            a = getDb(json_db)
            a.addMany([i for i in reader])


def convert_db_to_csv(db: str, targetcsv: str = "converted.csv") -> None:
    """
    Converts a JSON database to a csv.
    :param str db: path of the target json file
    :param str targetcsv: path of the converted csv ,default : converted.csv
    """
    if db.endswith(".json") and Path(db).is_file() is True:
        a = getDb(db)
        dict_data = a.getAll()
        data: List[Any] = [dict_data[i] for i in dict_data]
        headers = data[0].keys()

        with open(targetcsv, "w", newline="") as f:
            dict_writer: Any = csv.DictWriter(f, headers)
            dict_writer.writeheader()
            dict_writer.writerows(data)


def merge(p_file: str, m_file: str, output_file: Optional[str] = None) -> None:
    """
    Merges two json DB with the same schema
    :param str p_file: The primary file
    :param str m_file: The file to combine with p_file
    :param str output_file: The name of the output file, default: p_file
    """

    def verify_file(
        file_data: Dict[str, Dict[str, Any]], refer_keys: List[str], filename: str
    ) -> None:
        for d in file_data:
            temp_keys = list(file_data[d].keys())
            temp_keys.sort()
            if not temp_keys == refer_keys:
                print(f"Irregularities in key names in database {filename!r}")
                quit()

    o_file = output_file or p_file
    with open(p_file, "r") as p, open(m_file) as m:
        try:
            p_data = json.load(p)
            m_data = json.load(m)

            # look up primary data: a reference to the first data entry
            lp_data = list(p_data.values())[0]
            lm_data = list(m_data.values())[0]

            # verify that all the entries in each DB have the same keys
            p_keys = sorted(list(set(lp_data)))
            m_keys = sorted(list(set(lm_data)))

            verify_file(p_data, p_keys, p_file)
            verify_file(m_data, m_keys, m_file)

        except KeyError:
            print("Oops, the DB's does not follow the required PysonDb schema.")
            quit()
        except IndexError:
            print("One of the Database is empty")
            quit()

    # merge the two DB together

    if len(lp_data) == len(lm_data):
        if all(i in lm_data for i in lp_data):

            p_data.update(m_data)

            with open(o_file, "w") as f:
                print(p_data)
                json.dump(p_data, f)
        else:
            print("The keys of the Database entries does not match")
    else:
        print("The number keys in DB entries does not match")
    pass


def totwo(primary_file: str, output_file: Optional[str] = None) -> None:
    """Convert the old schema style DB to the new style"""

    if not Path(primary_file).is_file():
        print("The file does not exist")
        quit()

    with open(primary_file, "r") as f:
        try:
            new_data: Dict[str, Dict[str, Any]] = {}
            file_contents = json.load(f)
            file_data = file_contents["data"]

            for d in file_data:
                _id = d.pop("id")
                new_data[_id] = d

            with open(output_file or "converted_data.json", "w") as f:
                json.dump(new_data, f, indent=4)

        except Exception:
            print("something went wrong")
            quit()


def main() -> None:
    fire.Fire(
        {
            "create": create_if_not_exist,
            "display": display,
            "delete": delete,
            "convert": convert,
            "converttocsv": convert_db_to_csv,
            "merge": merge,
            "totwo": totwo
        }
    )


if __name__ == "__main__":
    main()
