<h1 align="center"><u>PysonDB</u></h1>

* [Install](https://github.com/fredysomy/pysonDB)
* [Example Code](https://github.com/fredysomy/pysonDB/example)
* [Command Line Operations](https://markdownitweb.herokuapp.com/cli-0e4d)
* [Adding Data](https://markdownitweb.herokuapp.com/add_data-c37f)
* [Get data](http://markdownitweb.herokuapp.com/getdata-fd3b)
* [Update Data](https://markdownitweb.herokuapp.com/updatedata-fd97)
* [Delete Data](https://markdownitweb.herokuapp.com/deletedata-6ead)


<h3>CLI Commands</h3>

* pysondb create [name]
  * [name] => name of json file.
* pysondb delete [name] 
  * [name] => name of json file. 
* pysondb display [name] 
  * [name] => name of json file.

<h3>Use</h3>

<h4><code> pysondb create [name]</code></h4>

```bash
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\Admin\Desktop\pysondb>pysondb create filedb.json
Succesfull created filedb.json in the directory.

```

<h4><code> pysondb delete [name]</code></h4>

```bash
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\Admin\Desktop\pysondb>pysondb delete file2.json
Do you want to remove the json file..(y/n)y
File deleted.

C:\Users\Admin\Desktop\pysondb>pysondb delete filedb.json
Do you want to remove the json file..(y/n)n
Action terminated
```
<h4><code> pysondb display [name]</code></h4>

File: filedb.json
```json
{"data": [{"name": "PysonDB", "type": "DB", "score": "10", "id": 5161221802}, {"name": "Pyson-CLI", "type": "CLI", "score": "10", "id": 2242313690}, {"name": "TinyDb", "type": "DB", "score": "9", "id": 6991190264}, {"name": "QWERTY", "type": "DB", "score": "5", "id": 9416036202}]}
```
Code.
```bash
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\Admin\Desktop\pysondb>pysondb display filedb.json
+-----------+------+-------+------------+
|   name    | type | score |     id     |
+-----------+------+-------+------------+
|  PysonDB  |  DB  |  10   | 5161221802 |
+-----------+------+-------+------------+
| Pyson-CLI | CLI  |  10   | 2242313690 |
+-----------+------+-------+------------+
|   Tiny    |  DB  |   9   | 6991190264 |
+-----------+------+-------+------------+
|  QWERTY   |  DB  |   5   | 9416036202 |
+-----------+------+-------+------------+
```

***

* See full examples [here](https://github.com/fredysomy/pysonDB/example).
* If You have any queries or doubts join the discord server [here](https://discord.gg/SZyk2dCgwg)

  
      