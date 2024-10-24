#Roldan Capponi Maximiliano

from Parcial_lll import ingresar, eliminar, consultar, listar


print("Bienvenido al registro de Casa de Repuestos IADES\n")
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


    
