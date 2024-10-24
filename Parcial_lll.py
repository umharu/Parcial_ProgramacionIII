#Roldan Capponi Maximiliano

from pymongo import MongoClient

url = "mongodb+srv://m4r1obros2:m4r1obros2@cluster0.ngxow.mongodb.net/"

try:
    cliente = MongoClient(host=[url])
    response = cliente.server_info()
except Exception as e:
    print(e)
    exit(1)
print(f"La conexion ha sido exitosa, {response}")

print("Listando las bases de datos: ")
print(cliente.list_database_names())




import json
import os

def cargar():
    if os.path.exists('casa_repuesto.json'):
        with open('casa_repuesto.json', 'r') as archivo:
            return json.load(archivo)
    else:
        return {}

def guardar():
    with open('casa_repuesto.json', 'w') as archivo:
        json.dump(casa_respuesto, archivo, indent=4)

def eliminar(sku):
    if sku in casa_respuesto:
        del casa_respuesto[sku]
        print("Eliminado ok")
        guardar()
    else:
        print("El sku no esta o fue eliminado")

def listar():
    if casa_respuesto:
        for sku, recorrer in casa_respuesto.items():
            print(f"SKU: {sku}, Nombre: {recorrer['nombre']}, Marca: {recorrer['marca']}, Precio: {recorrer['precio']}, Compatible: {recorrer['compatible']}")
    else:
            print("No existe registro")

def consultar(sku):
    if sku in casa_respuesto:
        recorrer = casa_respuesto[sku]
        print(f"SKU: {sku}, Nombre: {recorrer['nombre']}, Marca: {recorrer['marca']}, Precio: {recorrer['precio']}, Compatible: {recorrer['compatible']}")
    else:
        print("SKU no existe")

def ingresar():
    sku = input("Ingrese SKU -8 digitos alfanumericos-: ")
    if len(sku) != 8 or not sku.isalnum():
        print("SKU debe ser un valor alfanumerico")
        return
    if sku in casa_respuesto:
        print("SKU ya existe")
        return
    nombre = input("Ingrese nombre del repuesto: ")
    marca = input("Ingrese marca: ")
    precio = int(input(f"ingrese precio de {marca}: "))
    compatible = input("Ingrese modelos compatibles: ")
    
    casa_respuesto[sku] = {
        "nombre": nombre,
        "marca" : marca,
        "precio" : precio,
        "compatible" : compatible,
    }
    guardar()  
    print("Ingreso exitoso")
    

    
print("Bienvenido al registro de Casa de Repuestos IADES")
casa_respuesto = cargar()

while True:
    print("\nMenu")
    print("1. Ingresar nuevo elemento")
    print("2. Eliminar elemento")
    print("3. Listar todos los elementos")
    print("4. Consultar por un SKU")
    print("5. Salir")
    opcion = input("Seleccione una opcion (de 1 a 5): ")
    
    if opcion == "1":
        ingresar()
        
    elif opcion == "2":
        sku = input("Ingrese SKU a eliminar: ")
        eliminar(sku)
    elif opcion == "3":
        listar()
        
    elif opcion == "4":
        sku = input("Ingrese SKU a consultar: ")
        consultar(sku)
    elif opcion == "5":
        print("Gracias por utilizar Casa de Respuestos IADES")
        break
    else:
        print("Opcion no esta en el menu, ingrese otra")
    
