from os import system
from funciones import *
system("cls")

#198
asientos_ocupados = []
asientos_disponibles = []
asientos = []


while True:
    print('''
    1.-Comprar pasajes
    2.-Mostrar ubicaciones disponibles
    3.-Ver listado de pasajeros
    4.-Buscar pasajero
    5.-Imprimir lista de pasajeros
    0.-Salir
''')
    opcion = input("Ingrese una opcion: ")
    match opcion:
        case "1":
            print("Comprar pasajes")
            comprar_pasajes()
        case "2":
            print("Mostrar ubicaciones disponibles")
            mostrar_ubicaciones_disponibles()
        case "3":
            print("Ver listado de pasajeros")
            ver_listado_de_pasajeros()
        case "4":
            print("Buscar pasajero")
            buscar_pasajero()
        case "5":
            print("Imprimir lista de pasajeros")
            imprimir_lista_de_pasajeros()
        case "0":
            break
