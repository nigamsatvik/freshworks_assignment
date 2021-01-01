import threading
import json
import os
import sys
l = threading.Lock()
def create(key, value):  
    if len(key)> 32:
        print("Key length exceeds maximum capacity")
        return
    if sys.getsizeof(value)>16*1024:
        print("Value exceeds the maximum limit")
        return
    path="/home/satvik/data"
    if(os.path.isfile(path+"/"+key+".json")):
        print("Filename already exists")
        return
    if(os.path.isdir(path)==False):
        os.mkdir(path)
    try:
        
        json_object = json.loads(value) 
    except ValueError as e: 
        print ("Not a valid JSON")
        return
    l.acquire()
    with open(path+"/"+key+".json", "w") as outfile: 
        outfile.write(value) 
    l.release()
    print("File Created")
    return

def readfile(key):
    path="/home/satvik/data"
    if(os.path.isdir(path)==False):
        print("path does not exist")
        return
    if(os.path.isfile(path+"/"+key+".json")==False):
        print("File does not exist")
    with open(path+"/"+key+".json", "r") as openfile:
        json_object = json.load(openfile)
        print(json_object)
    return
def delfile(key):
    path="/home/satvik/data"
    if(os.path.isfile(path+"/"+key+".json")==False):
        print("file does not exist")
    os.remove(path+"/"+key+".json")
    print("File deleted")
    return
    
