<h1 align="center"><u>PysonDB</u></h1>

* [Install](https://github.com/pysonDB/pysonDB#install) 
* [Example Code](https://github.com/pysonDB/pysonDB/tree/master/example) 
* [Command Line Operations](https://pysondb.github.io/pysonDB/docs/cli) 
* [Adding Data](https://pysondb.github.io/pysonDB/docs/add) 
* [Get data](https://pysondb.github.io/pysonDB/docs/get) 
* [Search data](https://pysondb.github.io/pysonDB/docs/re_search) 
* [Update Data](https://pysondb.github.io/pysonDB/docs/update) 
* [Delete Data](https://pysondb.github.io/pysonDB/docs/delete)

<h2>Search using Regex</h2>

* Methods
  * reSearch(key, regex, objectify=False)
  * Searches for the objects where the value of the key follows the given regex. 

***

>>JSON file:file.json

```json
{"data": [{"name": "pysondb", "type": "DB"},
        {"name": "pysondb-cli", "type": "CLI"},
        {"name": "fire", "type": "CLI"},
        {"name": "stuff.py", "type": "GUI"},
        {"name": "def23@c-py", "type": "TUI"},
        {"name": "stuff(py", "type": "GUI"},
]}
```

***  

<h2><code>reSearch(key, regex, objectify=False)</code></h2>

```python
>> from pysondb import db
>> a=db.getDb("file.json")
>> print(a.reSearch("name", r"\w{3}\d{2}@c-py"))
>> [{'name': 'def23@c-py', 'type': 'TUI', 'id': 200151702869331613}]
>> print(a.reSearch("name", "stuff\(py"))
[{'name': 'stuff(py', 'type': 'GUI', 'id': 115618300909661724}]
```

***

* See full examples [here](https://github.com/pysonDB/pysonDB/example).
* If You have any queries or doubts join the discord server [here](https://discord.gg/SZyk2dCgwg)
