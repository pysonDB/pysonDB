import fire
from pathlib import Path
import json
from beautifultable import BeautifulTable
import os
import csv
import random
def create(name):
    """ 
    The below function checks if there is a similar .json file
    If the file exists It does nothing and it will add the filename variable to the class. 
    But if the file is not present it will add {data:[]} and will add the filename variable to the class.
    """

    sdx=Path(name)
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
def convert(c,d):
    print("Reading data from {}".format(c))
    arr=[]
    with open (c) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for csvRow in csvReader:
            csvRow['id']=random.randint(1000000000,9999999999)
            arr.append(csvRow)


    print("Writing data into {}".format(d))
    x={}
    x["data"]=arr
    y=json.dumps(x)
    filetowrite=open(d,"w")
    filetowrite.write(y)
    filetowrite.close()
    print("Conversion Succesfull")

def main():
    fire.Fire({
        'create':create,
        'display':display,
        'delete':delete,
        'convert':convert
    })



if __name__ == '__main__':
    main()