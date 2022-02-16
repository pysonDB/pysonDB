<h1 align="center"><u>PysonDB</u></h1>

* [Install](https://github.com/pysonDB/pysonDB#install) 
* [Example Code](https://github.com/pysonDB/pysonDB/tree/master/example) 
* [Command Line Operations](https://pysondb.github.io/pysonDB/docs/cli) 
* [Adding Data](https://pysondb.github.io/pysonDB/docs/add) 
* [Get data](https://pysondb.github.io/pysonDB/docs/get) 
* [Search data](https://pysondb.github.io/pysonDB/docs/re_search) 
* [Update Data](https://pysondb.github.io/pysonDB/docs/update) 
* [Delete Data](https://pysondb.github.io/pysonDB/docs/delete)



<h3>CLI Commands</h3>

* pysondb create [name]
  * [name] => name of json file.
* pysondb delete [name] 
  * [name] => name of json file. 
* pysondb display [name] 
  * [name] => name of json file.
* pysondb convert [path of csv file] [path of json file]
  * `pysondb convert example.csv example.json`
    * Creates an example.json file with converted data
* pysondb converttocsv [path of json file] [optional name for target CSV file]
  * `pysondb converttocsv example/registry.json`
    * Creates a converted.csv file with converted data
  * `pysondb converttocsv example/registry.json target.csv`
    * Creates a target.csv with the converted data.
* pysondb merge [path of primary json file] [path of json file to merge] [optional name for target json file]
  * `pysondb merge primary.json seconday.json`
    * Merges seconday.json data into primary.json
  * `pysondb merge primary.json seconday.json new.json`
    * Merges seconday.json and primary.json data into new.json

<h3 id="convert">Use</h3>
<h4><code> pysondb convert [csv file destination] [json file to write]</code></h4>

```cmd
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\Admin\Desktop\pysondb>pysondb convert file.csv file.json
Reading data from file.csv
Writing data into file.json
Conversion Succesfull


```

<h4><code> pysondb create [name]</code></h4>

```cmd
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\Admin\Desktop\pysondb>pysondb create filedb.json
Succesfull created filedb.json in the directory.

```

<h4><code> pysondb delete [name]</code></h4>

```cmd
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\Admin\Desktop\pysondb>pysondb delete file2.json
Do you want to remove the json file..(y/n)y
File deleted.

C:\Users\Admin\Desktop\pysondb>pysondb delete filedb.json
Do you want to remove the json file..(y/n)n
Action terminated
```

<h4><code> pysondb converttocsv [path.json] [target.csv]</code></h4>

```bash
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\Admin\Desktop\pysondb>pysondb converttocsv example/registry.json 
File converted and saving to  converted.csv
C:\Users\Admin\Desktop\pysondb>pysondb converttocsv example/registry.json filenew.csv
File converted and saving to  filenew.csv
```



<h4><code> pysondb display [name]</code></h4>

File: filedb.json
```json
{
  "data": [
    {
      "name": "PysonDB",
      "type": "DB",
      "score": "10",
      "id": 5161221802
    },
    {
      "name": "Pyson-CLI",
      "type": "CLI",
      "score": "10",
      "id": 2242313690
    },
    {
      "name": "TinyDb",
      "type": "DB",
      "score": "9",
      "id": 6991190264
    },
    {
      "name": "QWERTY",
      "type": "DB",
      "score": "5",
      "id": 9416036202
    }
  ]
}
```
Code
```cmd
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

* See full examples [here](https://github.com/pysonDB/pysonDB/tree/master/example).
* If You have any queries or doubts join the discord server [here](https://discord.gg/SZyk2dCgwg)

Example
```bash
gitpod/workspace/pysonDB$ pysondb converttocsv example/registry.json 
File converted and saving to  converted.csv

gitpod /workspace/pysonDB$ pysondb converttocsv example/registry.json filenew.csv
File converted and saving to  filenew.csv
```
