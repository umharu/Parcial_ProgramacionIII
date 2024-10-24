#Roldan Capponi Maximiliano

from pymongo import MongoClient

url = "mongodb+srv://m4r1obros2:m4r1obros2@cluster0.ngxow.mongodb.net/"

#Bloque Try para verificar la exitosa conexion a la DB 
try:
    cliente = MongoClient(host=[url])
    response = cliente.server_info()
except Exception as e:
    print(e)
    exit(1)
print(f"La conexion ha sido exitosa, {response}")

print("Listando las bases de datos: ")
#Lista el nombre de las bases de datos 
print(cliente.list_database_names())

print("Conectando a : 'IADES2024' ")

db = cliente['IADES2024']

#Se listan las collections
db_collections = db.list_collection_names()  

print(f"la coleccion seleccionada es: {db_collections[0]}")

db_col = db['Programacion_III']

cursor = db_col.find({})

for document in cursor:
    print(document)
    
