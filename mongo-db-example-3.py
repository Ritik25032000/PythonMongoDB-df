from pymongo import MongoClient

client = MongoClient('localhost',27017)
mydb = client["EmployeeDB"]
mycol = mydb["personal"]


'''

# inserting multiple documents (records1)

mylist = [
    {"regno": "106", "studname": "GGG", "
    
'''

for x in mycol.find({},{"_id":0}):
    print(x)
    
