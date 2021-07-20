<h1 align="center"><u>PysonDB</u></h1>

* [Install](https://github.com/fredysomy/pysonDB)
* [Example Code](https://github.com/fredysomy/pysonDB/tree/master/example)
* [Command Line Operations](https://fredysomy.me/pysonDB/docs/cli)
* [Adding Data](https://fredysomy.me/pysonDB/docs/add)
* [Get data](https://fredysomy.me/pysonDB/docs/get)
* [Search data](https://fredysomy.me/pysonDB/docs/re_search)
* [Update Data](https://fredysomy.me/pysonDB/docs/update)
* [Delete Data](https://fredysomy.me/pysonDB/docs/delete)
* [Image Utils](https://fredysomy.me/pysonDB/docs/image_utils)

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
```

***

* See full examples [here](https://github.com/fredysomy/pysonDB/example).
* If You have any queries or doubts join the discord server [here](https://discord.gg/SZyk2dCgwg)
