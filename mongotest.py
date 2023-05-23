from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://manasakuruba58:Manu$$5478@cluster0.dmrm3bf.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
print(client)

d = {
    "name":"manasa",
    "emailid":"manu1234@gmail.com",
    "surname":"kuruba"
}
db1 = client['mongotest']
col1 = db1['test']
col1.insert_one(d)