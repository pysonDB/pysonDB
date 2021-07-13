# pysonDB

### _Changelog_

* `dev`
  * New exceptions: `DataNotFoundError`, `IdNotFoundError`, `SchemaError`
  * YAML support
  * New database classes: `Database`, `UuidDatabase`, `YamlDatabase`, `YamlUuidDatabase`
  * Add lint to GitHub Actions
* `0.6.0`
  * Resloveed the error when automatically creating a DB
  * Added UUID Support.
  * Fixed all the bugs in v0.5.0

* `0.7.0`
  * Added DB to CSV conversion tool as a CLI.

* `0.7.4`
  * Fixed `name` not defined error in `cli.py`

* `0.8.0`
  * Fixed `name` not defined error in `cli.py`

* `0.9.0`
  * Added merge command to the cli tool



* `1.0.3`
  * Added a kwarg log to the JsonDatabase class to stop the log
  * Adde a kwarg objectify to all the get and search methods to convert json to python objects
  
* `1.1.0`
  * Added image saving and retrieving method in pysonDB
  * Added `add_image` function and `get_image` functions.

* `1.1.6`
  * Added a default indentation of `indent=3` to all dump function
