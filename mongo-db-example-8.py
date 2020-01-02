# find documents(S) with the address starting "x"

# import mongo client to connectivvity
from pymongo import MongoClient
# Creating instance of mongoclient
client = MongoClient('localhost',27017)

# Creating database
mydb = client["EmployeeDB"]

# Creating collection
mycoll = mydb["personal"]

myquery = {"address":{"$regex" : "^a"}}

mydoc = mycoll.find(myquery)

for x in  mydoc:
    print(x)
    
