#Bienvenida
print("\n=== BIENVENIDO ===\n")
input("Ingresa tu nombre: ")

#Menu principal-Inicio del bucle
while True:
    print("\n=== MENU PRINCIPAL ===\n")
    print("1. Inicio del juego")
    print("2. Configuración")
    print("3. Salir del juego")

    opcion=int(input("\nSeleciona una opción: "))

    if opcion == 1:
        print("\nNivel 1")

    elif opcion == 2:
        print("\n1. Subir y bajar el volumen")
        print("2. Personaliza la serpiente")
        opcion2 = int(input("\nselecciona una opción: "))

        if opcion2 == 1:
            print("\n=== SUBE O BAJA EL VOLUMEN ===\n")
            print("1. Subir volumen")
            print("2. Bajar volumen")

            subopcion = int(input("\nSelecciona una opcion: "))

        elif opcion2 == 2:
            print("\n=== SELECIONA EL COLOR DE TU SERPIENTE ===\n")
            print("1. Rojo")
            print("2. Morado")
            print("3. Azul")
            print("4. Verde")
            print("5. Blanco")

            subopcion = int(input("\nselecciona una opcion: "))

    elif opcion == 3:
        print("\nEstas seguro de salir del juego?\n")
        print("1.SI")
        print("2.NO")
        opcion3=int(input("\nSelecciona una opción: "))

        if opcion3 == 1:
            print("\nSalida del juego")
            break

        elif opcion3 == 2:
            print("\nRegresar al menú")