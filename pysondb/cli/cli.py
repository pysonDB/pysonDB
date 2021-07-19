import csv
import json
import os
import random

from typing import Optional

import fire
from beautifultable import BeautifulTable


def create_if_not_exist(file_name: str):
    """
    Checks for the existence of the provided JSON DB.
    If it does not, this will add {data:[]}.
    :param str file_name: The absolute path to the DB file
    """
    if not os.path.exists(file_name):
        with open(file_name, "w") as db_file:
            db = {"data": []}
            json.dump(db, db_file)
        print("Succesfully created {} in the directory.".format(file_name))


def display(file_name: str):
    table = BeautifulTable()
    with open(file_name) as jsondoc:
        data = json.load(jsondoc)
        real_data = data["data"]
        header = list(data["data"][0].keys())
        for all_data in real_data:
            table.rows.append(list(all_data.values()))
        table.columns.header = header
        print(table)


def delete(file_name: str):
    if os.path.exists(file_name):
        x = input("Do you want to remove the json file..(y/n)")
        if x in ["y", "Y"]:
            os.remove(file_name)
        else:
            print("Action terminated")
    else:
        print("The file does not exist")


def convert(csv_file, json_db):
    print("Reading data from {}".format(csv_file))
    arr = []
    with open(csv_file) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for csvRow in csvReader:
            csvRow["id"] = random.randint(1000000000, 9999999999)
            arr.append(csvRow)
    print("Writing data into {}".format(json_db))
    x = {}
    x["data"] = arr
    with open(json_db, "w") as json_file:
        json.dump(x, json_file)
    print("Conversion successful")


def convert_db_to_csv(filename: str, targetcsv="converted.csv"):
    """
    Converts a JSON database to a csv.
    :param str filename: path of the target json file
    :param str targetcsv: path of the converted csv ,default : converted.csv
    """
    with open(filename, "r") as db:
        json_loaded = json.load(db)["data"]
        csv_file = open(targetcsv, "a")
        csv_writer = csv.writer(csv_file)
        header = json_loaded[0].keys()
        csv_writer.writerow(header)
        print("File converted and saving to ", targetcsv)
        for each in json_loaded:
            csv_writer.writerow(each.values())
        csv_file.close()


def merge(p_file: str, m_file: str, output_file: Optional[str] = None):
    """
    Merges two json DB with the same schema
    :param str p_file: The primary file
    :param str m_file: The file to combine with p_file
    :param str output_file: The name of the output file, default: p_file
    """

    def verify_file(file_data, refer_keys, filename):
        for d in file_data:
            temp_keys = list(set(d.keys()))
            temp_keys.sort()
            if not temp_keys == refer_keys:
                print(f"Irregularities in key names in database {filename!r}")
                quit()

    o_file = output_file or p_file
    with open(p_file, "r") as p, open(m_file) as m:
        try:
            p_data = json.load(p)["data"]
            m_data = json.load(m)["data"]

            # look up primary data: a reference to the first data entry
            lp_data = p_data[0]
            lm_data = m_data[0]

            # verify that all the entries in each DB have the same keys
            p_keys = list(set(lp_data.keys()))
            m_keys = list(set(lm_data.keys()))

            p_keys.sort()
            m_keys.sort()

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
        if all(i in lm_data.keys() for i in lp_data):
            temp_data = {"data": m_data + p_data}
            with open(o_file, "w") as f:
                json.dump(temp_data, f)
        else:
            print("The keys of the Database entries does not match")
    else:
        print("The number keys in DB entries does not match")


def main():
    fire.Fire(
        {
            "create": create_if_not_exist,
            "display": display,
            "delete": delete,
            "convert": convert,
            "converttocsv": convert_db_to_csv,
            "merge": merge,
        }
    )


if __name__ == "__main__":
    main()
