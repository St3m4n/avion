def buscar_pasajero():
    while True:
        Pasajero=int(input("ingrese el rut para ver los datos del pasajero"))
        if Pasajero == "123":
            print(f"{lista}")
        else:
            print("no se ah encontrado a este pasajero")