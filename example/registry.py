from pysondb import db

a = db.getDb("registry.json")
while True:
    name = input("Enter Name:")
    age = input("Enter type:")
    score = input("Enter Score:")
    a.add({"name": name, "type": age, "score": score})
    c = input("add more(y,n)")
    if c == "n":
        print(a.getAll())
        break
