# to delete a document

# import mongo client to connect
from pymongo import MongoClient # import mongo client to connectivvity

# Creating instance of mongoclient
client = MongoClient('localhost',27017)

# Creating database
mydb = client["EmployeeDB"]

# Creating collection
mycoll = mydb["personal"]


myquery={"address":"xyz colony dehradun"}

#mycoll.delete_one(myquery) #delete first occurence
mycoll.delete_many(myquery) # delete all occurence

for x in mycoll.find({},{"_id":0}):
    print(x)
    
