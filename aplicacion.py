import time
from config import COLORES, configuracion, limpiar_pantalla
from juego import iniciar_juego

def ejecutar_programa():
    limpiar_pantalla()
    print("\n=== BIENVENIDO AL JUEGO DE LA SERPIENTE ===\n")
    nombre = input("Escribe tu nombre: ")
    configuracion["nombre_jugador"] = nombre
    
    while True:
        limpiar_pantalla()
        print(f"""
{COLORES['VERDE']}=== MENU PRINCIPAL ==={COLORES['RESET']}

Jugador: {COLORES['AMARILLO']}{configuracion['nombre_jugador']}{COLORES['RESET']}

1. Jugar
2. Opciones
3. Salir""")
        
        try:
            opcion = int(input("\nElige una opcion: "))
        except:
            print("\nEso no es un numero valido.")
            time.sleep(1)
            continue
            
        if opcion == 1:
            limpiar_pantalla()
            print(f"""
{COLORES['VERDE']}=== ELEGIR NIVEL ==={COLORES['RESET']}

1. Facil
2. Medio
3. Dificil
4. Regresar""")
            
            try:
                nivel = int(input("\nCual nivel quieres? "))
            except:
                print("\nOpcion no valida.")
                time.sleep(1)
                continue
                
            if nivel == 4:
                continue
                
            if nivel < 1 or nivel > 3:
                print("\nEse nivel no existe.")
                time.sleep(1)
                continue
                
            limpiar_pantalla()
            print(f"Empezando nivel {nivel}...")
            time.sleep(1)
            iniciar_juego(nivel)
            
        elif opcion == 2:
            while True:
                limpiar_pantalla()
                print(f"""
{COLORES['VERDE']}=== OPCIONES ==={COLORES['RESET']}

1. Cambiar volumen
2. Cambiar color de serpiente
3. Regresar""")
                
                try:
                    opcion2 = int(input("\nElige: "))
                except:
                    continue

                if opcion2 == 1:
                    limpiar_pantalla()
                    print(f"Volumen actual: {configuracion['volumen']}")
                    print("1. Subir")
                    print("2. Bajar")
                    
                    try:
                        vol = int(input("Opcion: "))
                        if vol == 1:
                            nuevo = configuracion["volumen"] + 10
                            if nuevo > 100:
                                nuevo = 100
                            configuracion["volumen"] = nuevo
                            print("Volumen subido.")
                        elif vol == 2:
                            nuevo = configuracion["volumen"] - 10
                            if nuevo < 0:
                                nuevo = 0
                            configuracion["volumen"] = nuevo
                            print("Volumen bajado.")
                        time.sleep(1)
                    except:
                        pass
                        
                elif opcion2 == 2:
                    limpiar_pantalla()
                    print("Colores disponibles:")
                    print("1. Verde")
                    print("2. Azul")
                    print("3. Rojo")
                    
                    try:
                        col = int(input("Cual color? "))
                        if col == 1:
                            configuracion["color_serpiente"] = COLORES["VERDE"]
                        elif col == 2:
                            configuracion["color_serpiente"] = COLORES["AZUL"]
                        elif col == 3:
                            configuracion["color_serpiente"] = COLORES["ROJO"]
                        print("Color cambiado.")
                        time.sleep(1)
                    except:
                        pass
                
                elif opcion2 == 3:
                    break
                    
        elif opcion == 3:
            print("\nAdios!")
            break
