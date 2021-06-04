from pysondb import db
from PIL import Image
from io import BytesIO
class add_image:
    def __init__(self,name):
        self.name=name
        self.db=db.getDb(name)
    def show(self):
        print(self.db.getAll())