import json
import os

MY_DATA = ''

def newfile (*param):
    with open (MY_DATA,'w') as wf:
        json.dump(param[0],wf,indent=4)

def addData(*param):
    with open (MY_DATA,'r+') as rwf:
        data_file = json.load(rwf)
        if (len(param)> 1):
            data_file.update({param[0]:param[1]})
        else:
            data_file.update({param[0]})
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)
        rwf.close()

def eliminar(*param):
    data=list(param)
    data[1].pop(data[0])
    newfile(data[1])

def readfile():
    with open(MY_DATA,'r') as rf:
        return json.load(rf)
    
def checkfile(*param):
    data = list(param)
    if (os.path.isfile(MY_DATA)):
        if (len(param)):
            print("Base de datos cargada...")
            data[0].update(readfile())
        else:
            if len(param):
                newfile(data[0])
           