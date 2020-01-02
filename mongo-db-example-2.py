from pymongo import MongoClient

client = MongoClient('localhost',27017)
mydb = client["EmployeeDB"]
mycol = mydb["personal"]

'''
for x in mycol.find():
    print(x)
    print()
'''

#mycol.find().limit(5)

for x in mycol.find({},{"_id":0,"ecode":1,"ename":1}):
    print(x)
    print()
    

