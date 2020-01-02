# import mongo client to connect
from pymongo import MongoClient # import mongo client to connectivvity

# Creating instance of mongoclient
client = MongoClient('localhost',27017)

# Creating database
mydb = client["EmployeeDB"]

# Creating collection
mycoll = mydb["personal"]

myquery = {"address":{"$gt":"x"}}

mydoc = mycoll.find(myquery)

for x in  mydoc:
    print(x)
    
