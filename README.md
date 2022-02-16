![data](https://raw.githubusercontent.com/pysonDB/pysonDB/master/images/file2son.png?token=APXKHAH6EDEJ7RUG3QOD2OC7ZHQZG)






## A Simple, Lightweight, Efficent JSON based DataBase for Python
 
 [![PyPI version](https://badge.fury.io/py/pysondb.svg)](https://pypi.org/project/pysondb/)
[![Downloads](https://pepy.tech/badge/pysondb/month)](https://pepy.tech/project/pysondb)
 ![.github/workflows/Build.yml](https://github.com/pysonDB/pysonDB/workflows/.github/workflows/Build.yml/badge.svg)
 [![CodeFactor](https://www.codefactor.io/repository/github/pysondb/pysondb/badge)](https://www.codefactor.io/repository/github/pysondb/pysondb)
 [![Discord](https://img.shields.io/discord/781486602778050590)](https://discord.gg/SZyk2dCgwg)
 ![GitHub Repo stars](https://img.shields.io/github/stars/pysonDB/pysonDB?style=plastic)
 ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/pysonDB/pysonDB)
[![Downloads](https://static.pepy.tech/personalized-badge/pysondb?period=total&units=international_system&left_color=green&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/pysondb)
 
 ***
 

The current stable version is v1.6.1
```python
pip install pysondb==1.6.1
```

## Support the project here

<a href="https://www.buymeacoffee.com/fredysomy"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee.&emoji=&slug=fredysomy&button_colour=FFDD00&font_colour=000000&font_family=Poppins&outline_colour=000000&coffee_colour=ffffff"></a>
## Hacktoberfest

While we are accepting pull requests for Hacktoberfest, we will reject any low-quality PR's.

We are accepting PRs for:

* Packages - updating package versions, adding new packages
Documentation updates
* More features and fixes (Refer here)
* CLI/API improvements - Redoing the CLI to reduce the usage of CLI packages.
* We are planning to reduce the project dependencies and remove other unwanted API's.
### Checkout the active issues [here](https://github.com/pysonDB/pysonDB/issues) 

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


* [Install](https://github.com/pysonDB/pysonDB#install) 
* [Example Code](https://github.com/pysonDB/pysonDB/tree/master/example) 
* [Command Line Operations](https://pysondb.github.io/pysonDB/cli) 
* [Adding Data](https://pysondb.github.io/pysonDB/add) 
* [Get data](https://pysondb.github.io/pysonDB/get) 
* [Search data](https://pysondb.github.io/pysonDB/re_search) 
* [Update Data](https://pysondb.github.io/pysonDB/update) 
* [Delete Data](https://pysondb.github.io/pysonDB/delete)

## Install

```python
pip install pysondb
```
## Create a database

* You can create a database using CLI.
```bash
pysondb create database_name.json
```
* Or in the python file.

```python
from pysondb import db

a=db.getDb("db.json")
```

* The above piece of code will create a database with ``` {data:[]}``` in it.
* Even if the json file exists there is no problem.

See more Documentation [here](https://pysondb.github.io/pysonDB/)

## What makes pysonDB different

* CLI support to create,delete and display database.
* Unique Id automatically assigned for each JSON data added.
* Schema regularity is checked.

## What pysonDB can't do.

* Cannot store images,videos etc.

## TODO

- [X] CLI to convert CSV to pysonDB required json.
- [X] Use CSV file in the database.
- [X] Make the database available to use local servers (Flask,Django)

## Contributors.

<a href="https://github.com/pysonDB/pysonDB/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=pysonDB/pysonDB" />
</a>


## Projects using PysonDB

* [my-first-streamlit-app](https://github.com/mro-lht/my-first-streamlit-app)
* [PythonChallenge](https://github.com/Odenrir/PythonChallenge)
* [Task-Me-Up](https://github.com/Adwaith-Rajesh/Task-Me-Up)
* [bagel](https://github.com/HaithemSouala/bagel)
* [prox_community](https://github.com/Kavzor/prox_community)
* [USVBachelorProject](https://github.com/mhj5103/USVBachelorProject)
* [gardenwatering](https://github.com/erivansousa/gardenwatering)
* [cf_scraper](https://github.com/bobross419/cf_scraper)
<!---
* [Programozasi_kornyezetek](https://github.com/Remgax/Programozasi_kornyezetek)
-->








## Contributing

Whether reporting bugs, discussing improvements and new ideas or writing extensions: Contributions to pysonDB are welcome! Here's how to get started:

* Join Discord channel [Here](https://discord.gg/SZyk2dCgwg)
* Check for issues or open a issue or open a feature requests.
* Fork the repository on Github
* Create a new branch off the master branch.
* Write a test which shows that the bug was fixed or that the feature works as expected.
* Send a pull request to us and wait till it get merged.
