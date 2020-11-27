import json
from pathlib import Path
import random




class getDb:
    def __init__(self,filename):
        sdx=Path(filename)

        # The below function checks if there is a similar .json file
        # If the file exists It does nothing and it will add the filename variable to the class. 
        # But if the file is not present it will add {data:[]} and will add the filename variable to the class.
        print(sdx)
        try:
            x=open(sdx,'r+')
            yt=x.read()
            try:
                cd=json.loads(yt)
                d=cd['data']
                x.close()
                self.filename=filename
            except:
                xy={'data':[]}
                x.write(json.dumps(xy))
                x.close()
                self.filename=filename
        except:
            xy={'data':[]}
            y=open(sdx,'a')
            y.write(json.dumps(xy))
            y.close()
            self.filename=filename
    def add(self,data2):
        class SchemmaNotMatchError(Exception):
            pass
        error="""The data you have entered doesnt match with the previously entered data.\nPlease enter the data according to the schemma you entered at the first commit.\n Data you entererd={} \n Schemma={}"""
        with open(self.filename, "r+") as fi:
            data = json.load(fi)


            """
            This will check if the number of elements in the firstly added json is equal to the currently added data.
            This is done to check uniformity of data.
            Even though the user add nonuniform data.This will notify them.
            """
            
            try:
               
                x=len(data['data'][0])
                
                if list(data["data"][0].keys())==list(data2.keys())+["id"]:
                    uid=random.randint(1000000000,9999999999)
                    data2['id']=uid
                    data['data'].append(data2)
                    fi.seek(0)
                    json.dump(data, fi)
                    return(uid)
                else:
                    return("False")
            except:
                data2['id']=random.randint(1000000000,9999999999)
                data['data'].append(data2)
                fi.seek(0)
                json.dump(data, fi) 

    def addMany(self,data_add):
        with open(self.filename, "r+") as fi:
            data = json.load(fi)
            # Multiple Json in form of a list entry.
            # This will check if the number of elements in the firstly added json is equal to the currently added data.
            # This is done to check uniformity of data.
            # Even though the user add nonuniform data.This will notify them.

            
            try:
               
                x=len(data['data'][0])
                for ji in data_add:
                    if list(data["data"][0].keys())==list(ji.keys())+["id"]:
                        ji['id']=random.randint(1000000000,9999999999)
                        data['data'].append(ji)
                        fi.seek(0)
                        json.dump(data, fi)
                        
            except:
                type_data=list(data_add[0].keys())
                for ji2 in data_add:
                    if list(type_data)==list(ji2.keys()):
                        ji2['id']=random.randint(1000000000,9999999999)
                        data['data'].append(ji2)
                        fi.seek(0)
                        json.dump(data, fi)
                        
                   

    def getAll(self):

        # The getAll() function can get all the data available in the database selected>

        with open(self.filename, "r") as fi:
            data = json.load(fi)
        return(data['data'])   

    def get(self,num=1):

        # The get(n) function gets n number of data , and default is 1
        try:
            with open(self.filename, "r") as fi:
                data = json.load(fi)  
            data_retrun=[]  
            if num<=len(data['data']):
                for i in range(0,num):
                    data_retrun.append(data['data'][i])
                return(data_retrun) 
            else:
                print("The length you have given {} \n Length of the database items= {}".format(num,len(data['data'])))    
        except:
            return("False")        
    def getBy(self,qury):

        # getBy({query}) allows the user to select the data form database which matches some query given.
        # for eg. getBy({"name":"pysondb"}) returns all data form database having "name":"pysondb" in it

        with open(self.filename,'r') as g_data:
            x=json.load(g_data)
            r_data=[]
            
            for g_d in x["data"]:
                if(all(j in g_d and g_d[j] == qury[j] for j in qury)):
                    r_data.append(g_d)
                else:
                    pass
        return(r_data)                


    def updateById(self,id,data):

        # the updateById("idofdata",{query}) allows the user to update the value of a key-value pair 

        errormsg="""The data given to update = {}  is not found as a subset of the data originally there = {}.\nYou tried to update values of keys in the database that doesnt exist\nPlease try again with correct keys."""
        with open(self.filename,"r+") as db:
            x=json.load(db)
            y=x["data"]
            df=[]
            if(set(list(data.keys())).issubset(set(list(y[0].keys())))):
                for f in y:
                    if f["id"]==int(id):
                        f.update(data)
                        df.append(f)
                    else:
                        df.append(f)
                x["data"]=df  
                db.seek(0)
                db.truncate()
                json.dump(x,db)
                return("True")
            else:
                print(errormsg.format(list(data.keys()),list(y[0].keys())))
                return("False")

    def deleteById(self,id):

        # the updateById("idofdata") allows the user to delete the data of a JSON doc of the given ID.

        error_del="""The Id given = {} is not found in the database \n available Id's are =>\n {}"""
        with open(self.filename,"r+") as db_del:
            x_del=json.load(db_del)
            y_del=x_del["data"]
            df_del=[]
            ids=[]
            for dataid in y_del:
                ids.append(str(dataid["id"]))

            try:
                for f_del in y_del:
                    if f_del["id"]==int(id):
                        pass
                    else:
                        df_del.append(f_del)
                x_del["data"]=df_del 
                db_del.seek(0)
                db_del.truncate()
                json.dump(x_del,db_del)
            except:    
                return False    
    def update(self,key2,query2):

        with open(self.filename,"r+") as updt:
            x_updt=json.load(updt)
            y_u=x_updt["data"]
            d_u=[]
            if(set(list(key2.keys())).issubset(set(list(y_u[0].keys()))) and set(list(query2.keys())).issubset(set(list(y_u[0].keys())))):
                for dat in y_u:
                    if(all(k in dat and dat[k] == key2[k] for k in key2)):
                        if(set(list(query2.keys())).issubset(set(list(y_u[0].keys())))):
                            dat.update(query2)
                            d_u.append(dat)
                           
                        else:
                            d_u.append(dat)
                            print("The given key for updation is not found in the database.\nPlease try again")    
                    else:
                        d_u.append(dat)
                       
                x_updt["data"]=d_u  
                updt.seek(0)
                updt.truncate()
                json.dump(x_updt,updt)    
            else:
                return("False")


            


               
               


            
                

       


        