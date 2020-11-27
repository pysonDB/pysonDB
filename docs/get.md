<h1 align="center"><u>PysonDB</u></h1>


* [Install](https://github.com/fredysomy/pysonDB) 
* [Example Code](https://github.com/fredysomy/pysonDB/example) 
* [Command Line Operations](https://markdownitweb.herokuapp.com/cli-0e4d) 
* [Adding Data](https://markdownitweb.herokuapp.com/add_data-c37f) 
* [Get data](http://markdownitweb.herokuapp.com/getdata-fd3b) 
* [Update Data](https://markdownitweb.herokuapp.com/updatedata-fd97) 
* [Delete Data](https://markdownitweb.herokuapp.com/deletedata-6ead)


<h2>Get Data</h2>

* There are three methods to get data.
  * get(n)
  * getAll()
  * getBy()


<h2><code>get()</code></h2>

* returns only one data by default.

* get(3) => retruns 3 json data. 

path.json

```json
{"data":[{"name":"pysondb","type":"DB"},{"name":"py_cli","type":"CLI"},{"name":"py_cli2","type":"CLI"}]}
```

```python
>> from pysondb import db
>> a=db.getDb("path.json")
>> a.get()
>> [{"name":"pysondb","type":"DB"}]
>> a.get(1)
>> [{"name":"pysondb","type":"DB"},{"name":"py_cli","type":"CLI"}]

```
<h2><code>getAll()</code></h2>

* Returns all data in the database

```python
>> from pysondb import db
>> a=db.getDb("path.json")
>> a.getAll()
>> [{"name":"pysondb","type":"DB"},{"name":"py_cli","type":"CLI"},{"name":"py_cli2","type":"CLI"}]

```
<h2><code>getBy(query)</code></h2>

* getBy(query)  query must be a JSON data.
* getBy({"type":"CLI"})

```python
>> from pysondb import db
>> a=db.getDb("path.json")
>> a.getBy({"type":"CLI"})
>> [{"name":"py_cli","type":"CLI"},{"name":"py_cli2","type":"CLI"}]
>> a.getBy({"name":"py_cli"})
>> [{"name":"py_cli","type":"CLI"}]


```

* See full examples [here](https://github.com/fredysomy/pysonDB/example). 
* If You have any queries or doubts join the discord server [here](https://discord.gg/SZyk2dCgwg)