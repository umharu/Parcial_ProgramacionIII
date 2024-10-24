#Roldan Capponi Maximiliano
 
from pymongo import MongoClient

#Variable de conexion
url = "mongodb+srv://m4r1obros2:m4r1obros2@cluster0.ngxow.mongodb.net/"

#Bloque Try para verificar la conexion a la DB 
try:
    cliente = MongoClient(host=[url])
    response = cliente.server_info()
except Exception as e:
    print(e)
    exit(1)
print(f"La conexion ha sido exitosa, {response}\n")

db = cliente['IADES2024'] #Base de datos 
db_col = db['Programacion_III'] #Coleccion 

#Funciones 
def eliminar(sku):
    eliminado = db_col.delete_one({'SKU': sku})
    if eliminado.deleted_count > 0:
        print("eliminado ok")
    else:
        print("El SKU no esta o fue eliminado")

def listar():
     listados = db_col.find()
     if db_col.count_documents({}) > 0:
         for listado in listados:
             print(f"SKU: {listado['SKU']}, Nombre: {listado['nombre']}, Marca: {listado['marca']}, Precio: {listado['precio']}, Compatible: {listado['compatible']}")
     else:
             print("No existe")

def consultar(sku):
    listado = db_col.find_one({'SKU': sku})
    if listado:
        print(f"SKU: {sku}, Nombre: {listado['nombre']}, Marca: {listado['marca']}, Precio: {listado['precio']}, Compatible: {listado['compatible']}")
    else:
        print("SKU no existe")

def ingresar():
    sku = input("Ingrese SKU -8 digitos alfanumericos-: ")
    if len(sku) != 8 or not sku.isalnum():
        print("El SKU debe ser alfanumerico. ")
        return
    if db_col.find_one({'SKU': sku}):
        print("SKU ya existe")
        return
    nombre = input("Ingrese nombre del respuesto: ")
    marca = input("Ingrese marca: ")
    precio = float(input(f"Ingrese el precio del {marca}: "))
    compatible = input("Ingrese modelo compatible: ")
    nuevo_listado = {
    'SKU': sku, 
    'nombre': nombre,
    'marca': marca,
    'precio': precio,
    'compatible': compatible
}
    db_col.insert_one(nuevo_listado)
    print("Ingreso exitoso")
