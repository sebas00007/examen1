concesionario = {}

while True:
    print("\nOpciones:")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1/2/3/4): ")
    
    if opcion == '1':
        marca = input("Ingrese la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")
        precio = input("Ingrese el precio del vehículo: ")
        
        detalles = {

            'Marca': marca,
            'Modelo': modelo,
            'Precio': precio
        }
        
        concesionario[marca] = detalles
        print(f"El vehículo '{marca}' ha sido agregado al concesionario.")
    
    elif opcion == '2':
        marca = input("Ingrese la marca del vehículo a buscar: ")

        if marca in concesionario:
            detalles = concesionario[marca]
            print(f"Detalles del vehículo '{marca}':")

            for clave, valor in detalles.items():
                print(f"{clave}: {valor}")
        else:
            print(f"El vehículo '{marca}' no se encuentra en el concesionario.")
    
    elif opcion == '3':
        marca = input("Ingrese la marca del vehículo a eliminar: ")

        if marca in concesionario:
            del concesionario[marca]
            print(f"El vehículo '{marca}' ha sido eliminado del concesionario.")
            
        else:
            print(f"El vehículo '{marca}' no se encuentra en el concesionario.")
    
    elif opcion == '4':
        break
    
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

