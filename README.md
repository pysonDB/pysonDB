

![data](https://raw.githubusercontent.com/fredysomy/pysonDB/master/images/file2son.png?token=APXKHAH6EDEJ7RUG3QOD2OC7ZHQZG)






## A Simple, Lightweight, Efficent JSON based DataBase for Python
 
 [![PyPI version](https://badge.fury.io/py/pysondb.svg)](https://badge/pysondb)
 ![PyPI - Downloads](https://img.shields.io/pypi/dm/pysondb)
 ![.github/workflows/Build.yml](https://github.com/fredysomy/pysonDB/workflows/.github/workflows/Build.yml/badge.svg)
 [![CodeFactor](https://www.codefactor.io/repository/github/fredysomy/pysondb/badge?s=a6ba6d3cb7fd5a89bbfab163b1f9b370df61ea5f)](https://www.codefactor.io/repository/github/fredysomy/pysondb)
 [![Discord](https://img.shields.io/discord/781486602778050590)](https://discord.gg/SZyk2dCgwg)
 ![GitHub Repo stars](https://img.shields.io/github/stars/fredysomy/pysonDB?style=plastic)
 ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/fredysomy/pysonDB)

 
 ***
 
## Features

* __Lightweight__ JSON based database.
* Supports __CRUD__ commands.
* No Database drivers required.
* __Unique ID__ assigned for each JSON document added.
* Strict about __Schema__ of data added. 
* __Inbuilt CLI__ to delete,display,create JSON database.

```python
>> from pysondb import db
>> a=db.getDb("path/to/json.json")
>> a.addMany([{"name":"pysondb","type":"DB"},{"name":"pysondb-cli","type":"CLI"}])
>> a.getAll()
>> [{"name":"pysondb","type":"DB"},{"name":"pysondb-cli","type":"CLI"}]
```
* See its simple..

## Quick Links


* [Install](https://github.com/fredysomy/pysonDB) 
* [Example Code](https://github.com/fredysomy/pysonDB/example) 
* [Command Line Operations](https://markdownitweb.herokuapp.com/cli-0e4d) 
* [Adding Data](https://markdownitweb.herokuapp.com/add_data-c37f) 
* [Get data](https://markdownitweb.herokuapp.com/getdata-fd3b) 
* [Update Data](https://markdownitweb.herokuapp.com/updatedata-fd97) 
* [Delete Data](https://markdownitweb.herokuapp.com/deletedata-6ead)

## Install

```python
pip install pysondb
```
## Create a database

* You can create a database usinf CLI.
```bash
pysondb create database_name
```
* Or in the python file.

```python
from pysondb import db

a=db.getDb("db.json')
```

* The above piece of code will create a database with ``` {data:[]}``` in it.
* Even if the json file exists there is no problem.

See more Documentation [here](https://markdownitweb.herokuapp.com/maindocs-2d9c)

## What makes pysonDB different

* CLI support to create,delete and display database.
* Unique Id automatically assigned for each JSON data added.
* Schema regularity is checked.

## What pysonDB can't do.

* Cannot store images,videos etc.

## TODO

- [ ] CLI to convert CSV to pysonDB required json.
- [ ] Use CSV file in the database.
- [ ] Make the database available to use local servers (Flask,Django)

## Contributing

Whether reporting bugs, discussing improvements and new ideas or writing extensions: Contributions to pysonDB are welcome! Here's how to get started:

* Join Discord channel [Here](https://discord.gg/SZyk2dCgwg)
* Check for issues or open a issue or open a feature requests.
* Fork the repository on Github
* Create a new branch off the master branch.
* Write a test which shows that the bug was fixed or that the feature works as expected.
* Send a pull request to us and wait till it get merged.
