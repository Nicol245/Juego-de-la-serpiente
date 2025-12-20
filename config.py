import os

# Colores para la consola
COLORES = {
    "RESET": "\033[0m",
    "ROJO": "\033[91m",
    "MORADO": "\033[95m",
    "AZUL": "\033[94m",
    "VERDE": "\033[92m",
    "BLANCO": "\033[97m",
    "AMARILLO": "\033[93m",
}

# Configuracion del juego
configuracion = {
    "color_serpiente": COLORES["VERDE"],
    "volumen": 50,
    "nombre_jugador": "",
}

def limpiar_pantalla():
    # Si es Windows usa cls, si no clear
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def leer_tecla():
    # Solo funciona en Windows
    if os.name == "nt":
        import msvcrt
        
        # Si se presiono una tecla
        if msvcrt.kbhit():
            tecla = msvcrt.getch()
            # Teclas especiales (flechas)
            if tecla == b"\xe0":
                tecla = msvcrt.getch()
                if tecla == b"H":
                    return "arriba" 
                if tecla == b"P":
                    return "abajo"
                if tecla == b"K":
                    return "izquierda"
                if tecla == b"M":
                    return "derecha"
            # Salir con q
            elif tecla == b"q" or tecla == b"Q":
                return "salir"
    
    return None
