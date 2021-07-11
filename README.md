![data](https://raw.githubusercontent.com/fredysomy/pysonDB/master/images/file2son.png?token=APXKHAH6EDEJ7RUG3QOD2OC7ZHQZG)






## A Simple, Lightweight, Efficent JSON based DataBase for Python
 
 [![PyPI version](https://badge.fury.io/py/pysondb.svg)](https://badge/pysondb)
 [![PyPI download day](https://img.shields.io/pypi/dm/pysondb.svg)](https://pypi.python.org/pypi/pysondb)
 ![.github/workflows/Build.yml](https://github.com/fredysomy/pysonDB/workflows/.github/workflows/Build.yml/badge.svg)
 [![CodeFactor](https://www.codefactor.io/repository/github/fredysomy/pysondb/badge?s=a6ba6d3cb7fd5a89bbfab163b1f9b370df61ea5f)](https://www.codefactor.io/repository/github/fredysomy/pysondb)
 [![Discord](https://img.shields.io/discord/781486602778050590)](https://discord.gg/SZyk2dCgwg)
 ![GitHub Repo stars](https://img.shields.io/github/stars/fredysomy/pysonDB?style=plastic)
 ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/fredysomy/pysonDB)

 
 ***
 

The current stable version is v1.1.3
```python
pip install pysondb==1.1.3
```

## Support the project here

<a href="https://www.buymeacoffee.com/fredysomy"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee.&emoji=&slug=fredysomy&button_colour=FFDD00&font_colour=000000&font_family=Poppins&outline_colour=000000&coffee_colour=ffffff"></a>
 
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
* [Example Code](https://github.com/fredysomy/pysonDB/tree/master/example) 
* [Command Line Operations](https://fredysomy.me/pysonDB/docs/cli) 
* [Adding Data](https://fredysomy.me/pysonDB/docs/add) 
* [Get data](https://fredysomy.me/pysonDB/docs/get) 
* [Search data](https://fredysomy.me/pysonDB/docs/re_search) 
* [Update Data](https://fredysomy.me/pysonDB/docs/update) 
* [Delete Data](https://fredysomy.me/pysonDB/docs/delete)
* [Image Utils](https://fredysomy.me/pysonDB/docs/image_utils)


## Install

```python
pip install pysondb
```
## Create a database

* You can create a database using CLI.
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

See more Documentation [here](https://fredysomy.me/pysonDB)

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

<a href="https://github.com/fredysomy/pysonDB/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=fredysomy/pysonDB" />
</a>


## Projects using PysonDB

* [my-first-streamlit-app](https://github.com/mro-lht/my-first-streamlit-app)
* [PythonChallenge](https://github.com/Odenrir/PythonChallenge)
* [Task-Me-Up](https://github.com/Adwaith-Rajesh/Task-Me-Up)
* [Programozasi_kornyezetek](https://github.com/Remgax/Programozasi_kornyezetek)
* [bagel](https://github.com/HaithemSouala/bagel)
* [prox_community](https://github.com/Kavzor/prox_community)
* [USVBachelorProject](https://github.com/mhj5103/USVBachelorProject)
* [gardenwatering](https://github.com/erivansousa/gardenwatering)
* [cf_scraper](https://github.com/bobross419/cf_scraper)








## Contributing

Whether reporting bugs, discussing improvements and new ideas or writing extensions: Contributions to pysonDB are welcome! Here's how to get started:

* Join Discord channel [Here](https://discord.gg/SZyk2dCgwg)
* Check for issues or open a issue or open a feature requests.
* Fork the repository on Github
* Create a new branch off the master branch.
* Write a test which shows that the bug was fixed or that the feature works as expected.
* Send a pull request to us and wait till it get merged.
