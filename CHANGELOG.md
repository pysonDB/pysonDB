# pysonDB

### _Changelog_

- `dev`

  - New exceptions: `DataNotFoundError`, `IdNotFoundError`, `SchemaError`
  - YAML support
  - New database classes: `Database`, `UuidDatabase`, `YamlDatabase`, `YamlUuidDatabase`
  - Add lint to GitHub Actions

- `0.6.0`

  - Resolved the error when automatically creating a DB
  - Added UUID Support.
  - Fixed all the bugs in v0.5.0

- `0.7.0`

  - Added DB to CSV conversion tool as a CLI.

- `0.7.4`

  - Fixed `name` not defined error in `cli.py`

- `0.8.0`

  - Fixed `name` not defined error in `cli.py`

- `0.9.0`

  - Added merge command to the cli tool

- `1.0.3`

  - Added a kwarg log to the JsonDatabase class to stop the log
  - Added a kwarg objectify to all the get and search methods to convert json to python objects

- `1.1.0`

  - Added image saving and retrieving method in pysonDB
  - Added `add_image` function and `get_image` functions.

- `1.1.6`

  - Added a default indentation of `indent=3` to all dump function

- `1.2.0`

  - Added `find(id) method`
    - It returns the dict if ID is found, else it raises IdNotFound error

- `1.4.0`

  - renamed

    - find -> getById
    - update -> updateByQuery
    - getBy -> getByQuery

  - removed updateArray

- `1.5.0`

  - Bug fixes

    - Removed bug in find (getById) function

  - Enhancements

    - Removed imageutils
    - Added argparse instead of Fire in CLI

  - Tests modified

- `1.5.1`

  - Enhancements
    - Optimised the `addMany` method of JsonDatabase
    - Example uses added in parser.help()
    - Typo in CLI fixed.

- `1.5.2`

  - Declarative meta data and typo fix
  - error handling when displaying database and database is null
  - error handling when converting to csv database and database is null

- `1.5.3`

  - Rename CLI command display to show. For ease of use and consistency.
  - Define database file extension in README.md and example uses.
  - Correct file location of CHANGELOG.md in pull request template.

- `1.5.4`

  - Fixed bug in CLI, grammar / typo fix

- `1.5.5`

  - Fixed broken links & fixed typos in docs / code 
  - Fixed broken link of code factor
  - Fixed broken links in README.md
  - Update unit test tests_db.py
  - Add new unit test in tests_db.py

- `1.5.7`
  - Update tests_getDb.py
  - Create new test tests_cli.py
  - Add schema error handling in addMany function
  - Add pypi project link in pypi package badge
  - Update repo url in docs and setup.cfg
- `1.6.0`
  - Update the tests
  - moved the errors into a seperate folder  

- `1.6.2`
  - Added missing __init__.py file.

- `1.6.3`
  - Fixed unicode being encoded as ASCII
- `1.6.4`
  - Updated links in documentation
