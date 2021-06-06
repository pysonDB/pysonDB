from pysondb import db
import os
import base64

class PathNotFoundError(Exception):
    """Exception raised for non-existent image path."""

    def __init__(self, *args):
        self.args = args

class NoNameError(Exception):
    """Exception raised when no name is passed as params along with the add_image function """

    def __init__(self, *args):
        self.args = args
class SaveError(Exception):
    """Exception raised when there is a error in saving the image"""

    def __init__(self, *args):
        self.args = args

class set:
    def __init__(self,db_name):
        self.db_name=db_name
        self.db=db.getDb(db_name)


    def add_image(self,src,name):
        if(os.path.exists(src)):
           with open(src,"rb") as img_data:
                raw_data=base64.b64encode(img_data.read())
                if(name):
                    name_list=src.split("/")
                    self.db.add({"data":raw_data.decode('utf-8'),"name":name,"fname":name_list[len(name_list)-1]})
                    print(f"The image is stored in the database :{self.db_name}")
                else:
                    raise NoNameError("No name was passed with the params")
        else:
            raise PathNotFoundError("The src image could not be found")


    def get_image(self,name):
        if(name):
            try:
                img_data=self.db.getBy({"name":name})
                f=open(img_data[0]["fname"],"wb")
                f.write(base64.decodebytes(bytes(img_data[0]['data'],"utf-8")))
                f.close()
            except Exception as e:
                raise SaveError(e)

        else:
            raise NoNameError("No name found")    
