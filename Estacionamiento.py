#Programa de simulacion de un estacionamiento de autos
#Autor: Anthony Satuquinga

Espacios = 50
ingreso = 0
retiro = 0  
print("El estacionamiento tiene", Espacios, "espacios disponibles.")

while Espacios >= 0:
    print("""
    _________Opciones del Estacionamiento_________
    1. Ingresar un auto
    2. Retirar un auto
    3. Salir del estacionamiento
    ______________________________________________
    """)
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            if Espacios > 0:
                ingreso = int(input("Ingrese la cantidad de autos que desea ingresar: "))
                ingreso = ingreso
                if ingreso > Espacios:
                    print("No puede ingresar esa cantidad de Autos")
                    continue
                Espacios -= ingreso
                print(f"Ha ingresado {ingreso} autos. Espacios disponibles: {Espacios}")
            else:
                print("No hay espacios disponibles para ingresar autos.")
        case 2:
            if Espacios < 50:
                retiro = int(input("Ingrese la cantidad de autos que desea retirar: "))
                retiro = retiro
                if retiro > ingreso:
                    print("No puede retirar esa cantidad de Autos")
                    continue
                Espacios += retiro
                print(f"Ha retirado {retiro} autos. Espacios disponibles: {Espacios}")
            else:
                print("No hay autos para retirar.")
        case 3:
             print("Saliendo del estacionamiento...")
             break
        case _:
             print("Opcion invalida. Por favor, ingrese una opcion valida.")                  