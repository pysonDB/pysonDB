import argparse
import csv
import json
import os
import random
from typing import Optional, Sequence

from beautifultable import BeautifulTable


def create_if_not_exist(file_name: str) -> int:
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
        return 0

    return 1


def display(file_name: str) -> int:
    """
    Print a database file
    :param str file_name: The absolute path to the DB file
    """
    table = BeautifulTable()
    with open(file_name) as jsondoc:
        data = json.load(jsondoc)
        real_data = data["data"]
        header = list(data["data"][0].keys())
        for all_data in real_data:
            table.rows.append(list(all_data.values()))
        table.columns.header = header
        print(table)
    return 0


def delete(file_name: str) -> int:
    """
    Delete a database file
    :param str file_name: The absolute path to the DB file
    """
    if os.path.exists(file_name):
        x = input("Do you want to remove the json file..(y/n)")
        if x in ["y", "Y"]:
            os.remove(file_name)
            return 0

        else:
            print("Action terminated")
    else:
        print("The file does not exist")

    return 1


def convert(csv_file: str, json_db: str) -> int:
    """
    Convert a csv file to a JSON database file
    :param str csv_file: path of the target csv file
    :param str json_Db: path of the target json database
    """
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
    return 0


def convert_db_to_csv(filename: str, targetcsv: str) -> int:
    """
    Converts a JSON database to a csv.
    :param str filename: path of the target json file
    :param str targetcsv: path of the converted csv, default : converted.csv
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

    return 0


def merge(p_file: str, m_file: str, output_file: Optional[str] = None) -> int:
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
                return 1

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
            return 1

        except IndexError:
            print("One of the Database is empty")
            return 1

    # merge the two DB together

    if len(lp_data) == len(lm_data):
        if all(i in lm_data.keys() for i in lp_data):
            temp_data = {"data": m_data + p_data}
            with open(o_file, "w") as f:
                json.dump(temp_data, f)
        else:
            print("The keys of the Database entries does not match")
            return 1
    else:
        print("The number keys in DB entries does not match")
        return 1

    return 0


def set_parser(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(argv)
    subparsers = parser.add_subparsers(dest="command")

    create_parser = subparsers.add_parser("create", help="Create a new database file")
    create_parser.add_argument("file_name", help="Name of the database file")

    display_parser = subparsers.add_parser("display", help="Display a database file")
    display_parser.add_argument(
        "file_name", help="Name of the database file to display"
    )

    delete_parser = subparsers.add_parser("delete", help="Delete a database file")
    delete_parser.add_argument("file_name", help="Name of the database file to delete")

    convert_parser = subparsers.add_parser(
        "convert", help="Convert a csv file to a JSON database file"
    )
    convert_parser.add_argument("csv_file")
    convert_parser.add_argument("json_db")

    convert_to_csv_parser = subparsers.add_parser(
        "converttocsv", help="Converts a JSON database to a csv file"
    )
    convert_to_csv_parser.add_argument("file_name", help="path of the target json file")
    convert_to_csv_parser.add_argument(
        "-t",
        "--target_csv",
        help="path of the converted csv, default : converted.csv",
        default="converted.csv",
    )

    merge_parser = subparsers.add_parser("merge")
    merge_parser.add_argument("p_file", help="The primary file")
    merge_parser.add_argument("m_file", help="The file to combine with p_file")
    merge_parser.add_argument(
        "-o", "--output-file", help="The name of the output file, default: p_file"
    )

    args = parser.parse_args()

    if args.command == "create":
        return create_if_not_exist(args.file_name)

    elif args.command == "display":
        return display(args.file_name)

    elif args.command == "delete":
        return delete(args.file_name)

    elif args.command == "convert":
        return convert(args.csv_file, args.json_db)

    elif args.command == "converttocsv":
        return convert_db_to_csv(args.file_name, args.target_csv)

    elif args.command == "merge":
        return merge(args.p_file, args.m_file, args.output_file)

    else:  # show help menu if the cli was started without an argument
        parser.print_help()
        return 0


def main() -> int:
    return set_parser()


if __name__ == "__main__":
    raise SystemExit(main())
