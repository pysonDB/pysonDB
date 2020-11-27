<div align="center">
<img width="80%" src="https://raw.githubusercontent.com/fredysomy/pysonDB/master/images/file2son.png?token=APXKHAH6EDEJ7RUG3QOD2OC7ZHQZG">
</div>


<div align="center">

<h2>A Simple, Lightweight, Efficent JSON based DataBase for Python.</h2>

</div>

<div align="center">

 [![PyPI version](https://badge.fury.io/py/pysondb.svg)](https://badge/pysondb)
 ![PyPI - Downloads](https://img.shields.io/pypi/dm/pysondb)
 [![CodeFactor](https://www.codefactor.io/repository/github/fredysomy/pysondb/badge?s=a6ba6d3cb7fd5a89bbfab163b1f9b370df61ea5f)](https://www.codefactor.io/repository/github/fredysomy/pysondb)
 [![Discord](https://img.shields.io/discord/781486602778050590)](https://discord.gg/SZyk2dCgwg)
 ![GitHub Repo stars](https://img.shields.io/github/stars/fredysomy/pysonDB?style=plastic)
 ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/fredysomy/pysonDB)
 
 </div>
 
<h2>Features</h2>

* __Lightweight__ JSON based database.
* Supports __CRUD__ commands.
* No Database drivers required.
* __Unique ID__ assigned for each JSON document added.
* Strict about __Schemma__ of data added. 
* __Inbuilt CLI__ to delete,display,create JSON database.

```python
>> from pysondb import db
>> a=db.getDb("path/to/json.json")
>> a.addMany([{"name":"pysondb","type":"DB"},{"name":"pysondb-cli","type":"CLI"}])
>> a.getAll()
>> [{"name":"pysondb","type":"DB"},{"name":"pysondb-cli","type":"CLI"}]
```
* See its simple..

<h2>Quick Links</h2>

* [Documentation]()
* [Install]()
* [Example Code]()
* [Command Line Operations]()
* [Adding Data]()
* [Get data]()
* [Update Data]()
* [Delete Data]()

<h2 id="install">Install</h2>

```python
pip install pysondb
```
<h2>Create a database</h2>

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

See more Documentation [here]()

<h2>What makes pysonDB different</h2>

* CLI support to create,delete and display database.
* Unique Id automatically assigned for each JSON data added.
* Schemma regularity is checked.
<h2>What pysonDB can't do.</h2>

* Cannot store images,videos etc.

<h2>TODO</h2>

- [ ] CLI to convert CSV to pysonDB required json.
- [ ] Use CSV file in the database.
- [ ] Make the database available to use local servers (Flask,Django)

<h2>Contributing</h2>

Whether reporting bugs, discussing improvements and new ideas or writing extensions: Contributions to pysonDB are welcome! Here's how to get started:

* Join Discord channel [Here](https://discord.gg/SZyk2dCgwg)
* Check for issues or open a issue or open a feature requests.
* Fork the repository on Github
* Create a new branch off the master branch.
* Write a test which shows that the bug was fixed or that the feature works as expected.
* Send a pull request to us and wait till it get merged.


 

