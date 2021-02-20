from pysondb import db

a = db.getDb("test.json")


def addtests():
    x = a.add({"name": "test"})


def gettests():
    x = len(a.get(1))


def wrongaddtest():
    y = a.add({"namme": "sd"})
    assert y == "False"


def updatetest():
    a.update({"name": "test"}, {"name": "tests"})
    x = a.get()[0]["name"]
    assert x == "tests"


def deletetest():
    x = a.get()[0]["id"]
    a.deleteById(x)
    y = a.get()


if __name__ == "__main__":
    addtests()
    gettests()
    wrongaddtest()
    updatetest()
    deletetest()
    print("All tests have passed")
