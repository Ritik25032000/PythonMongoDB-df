#retreiving document from pers collection

from pymongo import MongoClient # import mongo client to connectivvity

client = MongoClient('localhost',27017)
mydb = client["EmployeeDB"]
mycoll = mydb["personal"]
x=mycoll.find({},{"_id":0,"address":1})

for i in x:
    print(i)

