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

<h2>Image Utils</h2>

* Methods
  * `add_image(src="path/to/image",name="nameoffile")`
    * Adds the image to the database
  * `get_image("nameoffile")`
    * Gets the image stored and saves it in the current directory.
***

>JSON file: file.json

```json
{"data": [{"name": "pysondb", "data":"asdsddfgdfdf45dvrtge...","fname":"file.png"}
]}
```

***  

<h2><code>add_image(src="path/to/image",name="nameoffile")</code></h2>

```python
>> from pysondb.imageutils import imageutils
>> a=imageutils.setdb("file.json") #the data of image will be stored here.
>> a.add_image(src="file.png",name="pysondb")
>> #The image is stored in the database :example/rere.json
>> a.get_image("pysondb")
>> # This command will save the image in the current directory.
```

***

* See full examples [here](https://github.com/fredysomy/pysonDB/example).
* If You have any queries or doubts join the discord server [here](https://discord.gg/SZyk2dCgwg)