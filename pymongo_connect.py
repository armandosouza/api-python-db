from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://multicodelab:<password>@cluster0.wg1jssh.mongodb.net/?retryWrites=true&w=majority")
db = client.pymongo
collection = db.bank

""" cliente = {
	"nome": "Armando Souza",
	"cpf": "123456789",
	"endereco": "Rua A"
}

cliente_post = collection.insert_one(cliente).inserted_id
print(cliente_post)
"""

for cliente in collection.find():
	pprint(cliente)