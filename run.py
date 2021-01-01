import code as x
import json
thisdict={
 "brand": "FORD",
 "model": "mustang",
 "year": "1964"
}

value=json.dumps(thisdict)
x.create("cardata" , value)
x.create("cardata" , value) #check duplicacy
x.create("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd", value)# key length
x.readfile("cardata")# read function
x.delfile("cardata")#delete 


