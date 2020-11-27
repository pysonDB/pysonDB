<div align="center">
<img width="80%" src="https://raw.githubusercontent.com/fredysomy/pysonDB/master/images/file2son.png?token=APXKHAH6EDEJ7RUG3QOD2OC7ZHQZG">
</div>

***
<div align="center">

<h2>A simple,lightweight,efficent JSON based database for python.</h2>

</div>

<h2>Features</h2>

* Lightweight JSON based database.
* Supports CRUD commands.
* No Database drivers required.
* Unique ID assigned for each JSON document added.
* Strict about Schemma of data added. 
* Inbuilt CLI to delete,display,create JSON database.

```python
>> from pysondb import db
>> a=db.getDb("path/to/json.json")
>> a.addMany([{"name":"pysondb","type":"DB"},{"name":"pysondb-cli","type":"CLI"}])
>> a.getAll()
>> [{"name":"pysondb","type":"DB"},{"name":"pysondb-cli","type":"CLI"}]
```
See its simple..

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
<h2>TODO</h2>

- [ ] Use CSV file in the database.
- [ ] Make the database available to use local servers (Flask,Django)

<h2>Contributing</h2>

Whether reporting bugs, discussing improvements and new ideas or writing extensions: Contributions to TinyDB are welcome! Here's how to get started:

* Check for issues or open a issue or open a feature requests.
* Fork the repository on Github
* Create a new branch off the master branch.
* Write a test which shows that the bug was fixed or that the feature works as expected.
* Send a pull request to us and wait till it get merged.


 

