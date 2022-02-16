<h1 align="center"><u>PysonDB</u></h1>

* [Install](https://github.com/pysonDB/pysonDB#install) 
* [Example Code](https://github.com/pysonDB/pysonDB/tree/master/example) 
* [Command Line Operations](https://pysondb.github.io/pysonDB/cli) 
* [Adding Data](https://pysondb.github.io/pysonDB/add) 
* [Get data](https://pysondb.github.io/pysonDB/get) 
* [Search data](https://pysondb.github.io/pysonDB/re_search) 
* [Update Data](https://pysondb.github.io/pysonDB/update) 
* [Delete Data](https://pysondb.github.io/pysonDB/delete)

<h2>Add Data</h2>

* Adding data is is simple.
* There are two methods to add data.
  * add()
  * addMany()
* The Schemma of data you add first is the schemma for the whole database.
* Adding data checks for Schemma regularity.
* And any Schemma irregularity rejects the irregular data.

<h2><code>add()</code></h2>

* add({"key":"value,"key":value})

* add(json)

```python
>> from pysondb import db
>> #from pysondb import getDb
>> #a=getDb("test.json")
>> a=db.getDb("pathtojson.json")
>> a.add({"name":"pysondb","type":"DB"})
>> # returns 1929323232 which is a ID assigned to the above data.
>> a.add({"namme":"pyson","type":"DB"})
>> # The data wont be added as the key "name" is mispelled as "namme"

```
<h2><code>addMany()</code></h2>

* addMany([{},{},...])

* addMany(list of dictionaries)

```python
>> from pysondb import db
>> a=db.getDb("pathtojson.json")
>> a.addMany([{"name":"pysondb","type":"DB"},{"name":"py_cli","type":"CLI"}])
>> # Both data is added in the database.
>> a.add([{"namme":"pyson","type":"DB"},{"name":"py_cli2","type":"CLI"}])

The first data wont be added as the key "name" is mispelled as "namme"
But the second data will be added.

>>a.getAll()
{"name":"pysondb","type":"DB"},{"name":"py_cli","type":"CLI"},{"name":"py_cli2","type":"CLI"}]
```
* See full examples [here](https://github.com/pysonDB/pysonDB/example).
* If You have any queries or doubts join the discord server [here](https://discord.gg/SZyk2dCgwg)
