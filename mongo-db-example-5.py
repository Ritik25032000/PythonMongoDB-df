# to update a document in collection

# import mongo client to connect
from pymongo import MongoClient # import mongo client to connectivvity

# Creating instance of mongoclient
client = MongoClient('localhost',27017)

# Creating database
mydb = client["EmployeeDB"]

# Creating collection
mycoll = mydb["personal"]


myquery ={"ecode":"102"}
newvalues = {"$set": {"ecode":"107"}}

#mycoll.update_one(myquery,newvalues)
mycoll.update_many(myquery , newvalues)

# display all documents

for x in mycoll.find({},{"_id":0}):
    print(x)
