<h1 align="center"><u>PysonDB</u></h1>


* [Example Code]()
* [Command Line Operations]()
* [Adding Data]()
* [Get data]()
* [Update Data]()
* [Delete Data]()


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

* See full examples [here]().
* If You have any queries or doubts join the discord server [here]()

 