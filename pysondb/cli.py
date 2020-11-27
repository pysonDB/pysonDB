import fire
from pathlib import Path
import json
from beautifultable import BeautifulTable
import os
def create(name):
    sdx=Path(name)
    
    """ 
    The below function checks if there is a similar .json file
    If the file exists It does nothing and it will add the filename variable to the class. 
    But if the file is not present it will add {data:[]} and will add the filename variable to the class.
    """

    
    if sdx.exists():
        x=open(name,'r+')
        yt=x.read()
        try:
            cd=json.loads(yt)
            d=cd['data']
            x.close()
            return("File exists")
            
        except:
            xy={'data':[]}
            x.write(json.dumps(xy))
            x.close()

    else:
        xy={'data':[]}
        y=open(name,'a')
        y.write(json.dumps(xy))
        y.close()
        return("Succesfull created {} in the directory.".format(name))
def display(name):
    table = BeautifulTable()
 
    with open(name,'r+') as jsondoc:
        
        data=json.load(jsondoc)
        real_data=data['data']
        header=list(data["data"][0].keys())
        for all_data in real_data:
            table.rows.append(list(all_data.values()))
        table.columns.header=header

        print(table)
def delete(name):
    if os.path.exists(name):
        x=input("Do you want to remove the json file..(y/n)")
        if x=="y" or x=="Y":
            os.remove(name)
        else:
            print("Action terminated")    
    else:
        print("The file does not exist")
def convert(csvfile,destfile):
    pass
def main():
    fire.Fire({
        'create':create,
        'display':display,
        'delete':delete
    })



if __name__ == '__main__':
    main()