<h1 align="center"><u>PysonDB</u></h1>

* [Install](https://github.com/fredysomy/pysonDB) 
* [Example Code](https://github.com/fredysomy/pysonDB/tree/master/example) 
* [Command Line Operations](https://fredysomy.me/pysonDB/docs/cli) 
* [Adding Data](https://fredysomy.me/pysonDB/docs/add) 
* [Get data](https://fredysomy.me/pysonDB/docs/get) 
* [Search data](https://fredysomy.me/pysonDB/docs/re_search) 
* [Update Data](https://fredysomy.me/pysonDB/docs/update) 
* [Delete Data](https://fredysomy.me/pysonDB/docs/delete)


<h2>Update Data</h2>

* Update command also check for Schemma.
* Schemma violating data will be rejected.
* Methods:
  * updateById(ID,query)
    * There is a unique ID assigned for each json data.
  * update(query,what_to_update)
    * update({"name":"pysondb"},{"name":"pyson"}).
    * Updates the all value of key "pysondb" to pyson

>>JSON file:file.json

```json
{"data": [{"name": "PysonDB", "type": "DB", "score": "10", "id": 5161221802},
{"name": "Pyson-CLI", "type": "CLI", "score": "10", "id": 2242313690},
{"name": "Tiny", "type": "DB", "score": "9", "id": 6991190264},
{"name": "QWERTY", "type": "DB", "score": "5", "id": 9416036202}]}
```

***

<h4><code>updateById(ID,what_to_update)</code></h4>

* ID=Integer

```python
>> from pysondb import db
>> a=db.getDb("file.json")
>> a.updateById("9416036202",{"name":"Qwerty12"})
>> a.getBy({"name":"Qwerty12"})
>> #In the file.json the data is updated.
>> #We can verify it below.
>> [{"name": "Qwerty12", "type": "DB", "score": "5", "id": 9416036202}]

```

<h4><code>update(query,what_to_update)</code></h4>

* query,what_to_update are both JSON data.

```python
>> from pysondb import db
>> a=db.getDb("file.json")
>> a.update({"name":"Pyson-CLI"},{"name":"PysonCLI"})
>> a.getBy({"name":"PysonCLI"})
>> # In the file.json the data is updated for all data where name=Pyson-CLI
>> # We can verify it below.
>> [{"name": "PysonCLI", "type": "CLI", "score": "10", "id": 2242313690}]


```

***

* See full examples [here](https://github.com/fredysomy/pysonDB/example). 
* If You have any queries or doubts join the discord server [here](https://discord.gg/SZyk2dCgwg)
