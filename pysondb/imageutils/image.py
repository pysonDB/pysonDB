from pysondb import db
from PIL import Image
from io import BytesIO
import os
import base64
class PathNotFoundError(Exception):
    """Exception raised for non-existent image path."""

    def __init__(self, *args):
        self.args = args

class image_utils:
    def __init__(self,db_name):
        self.db_name=db_name
        self.db=db.getDb(db_name)
    def add_image(self,src,name):
        if(os.path.exists(src)):
           with open(src,"rb") as img_data:
                raw_data=base64.b64encode(img_data.read())
                self.db.add({"data":raw_data.decode('utf-8'),"name":name})
        else:
            raise PathNotFoundError("fsfsdsfsf")