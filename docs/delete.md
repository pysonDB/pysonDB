<h1 align="center"><u>PysonDB</u></h1>

* [Install](https://github.com/pysonDB/pysonDB#install) 
* [Example Code](https://github.com/pysonDB/pysonDB/tree/master/example) 
* [Command Line Operations](https://pysondb.github.io/pysonDB/cli) 
* [Adding Data](https://pysondb.github.io/pysonDB/add) 
* [Get data](https://pysondb.github.io/pysonDB/get) 
* [Search data](https://pysondb.github.io/pysonDB/re_search) 
* [Update Data](https://pysondb.github.io/pysonDB/update) 
* [Delete Data](https://pysondb.github.io/pysonDB/delete)

<h2>Delete Data</h2>

* Methods
  * deleteById(ID)
  * Deletes the JSON data with the given ID 

***

>>JSON file:file.json

```json
{"data": [{"name": "PysonDB", "type": "DB", "score": "10", "id": 5161221802},
{"name": "Pyson-CLI", "type": "CLI", "score": "10", "id": 2242313690},
{"name": "Tiny", "type": "DB", "score": "9", "id": 6991190264},
{"name": "QWERTY", "type": "DB", "score": "5", "id": 9416036202}]}
```

***  

<h2><code>deleteById(ID)</code></h2>

```python
>> from pysondb import db
>> a=db.getDb("file.json")
>> a.deleteById("6991190264")
>> # The JSON data with ID "6991190264" is deleted.Lets verify.
>> a.getAll()
>> [{"name": "PysonDB", "type": "DB", "score": "10", "id": 5161221802},
{"name": "Pyson-CLI", "type": "CLI", "score": "10", "id": 2242313690},
{"name": "QWERTY", "type": "DB", "score": "5", "id": 9416036202}]
```

***

* See full examples [here](https://github.com/pysonDB/pysonDB/example).
* If You have any queries or doubts join the discord server [here](https://discord.gg/SZyk2dCgwg)
