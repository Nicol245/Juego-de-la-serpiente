import random
import time
from config import COLORES, configuracion, limpiar_pantalla, leer_tecla
from niveles import obtener_obstaculos, obtener_velocidad

def mostrar_fin_juego(razon, puntos):
    limpiar_pantalla()
    mensaje = str(razon)
    
    # Cortar mensaje si es muy largo
    if len(mensaje) > 26:
        mensaje = mensaje[:26]
    else:
        # Rellenar con espacios
        espacios = 26 - len(mensaje)
        mensaje = mensaje + (" " * espacios)

    print(f"""
{COLORES['ROJO']}╔════════════════════════════╗{COLORES['RESET']}
{COLORES['ROJO']}║   ¡PERDISTE!               ║{COLORES['RESET']}
{COLORES['ROJO']}║   {mensaje}║{COLORES['RESET']}
{COLORES['ROJO']}║   Puntos finales: {puntos:3d}      ║{COLORES['RESET']}
{COLORES['ROJO']}╚════════════════════════════╝{COLORES['RESET']}""")
    input("\nPresiona Enter para seguir...")

def crear_comida(alto, ancho, cuerpo_serpiente, lista_obstaculos):
    while True:
        # Elegir posicion al azar
        fila = random.randint(1, alto - 2)
        columna = random.randint(1, ancho - 2)
        posicion = [fila, columna]
        
        # Verificar que no caiga en la serpiente ni en obstaculos
        if posicion in cuerpo_serpiente:
            continue
            
        choca_obstaculo = False
        for obs in lista_obstaculos:
            if obs[0] == fila and obs[1] == columna:
                choca_obstaculo = True
                break
        
        if choca_obstaculo:
            continue
            
        return posicion

def dibujar(alto, ancho, cuerpo_serpiente, lista_obstaculos, pos_comida):
    # Crear matriz vacia
    matriz = []
    for f in range(alto):
        fila_nueva = []
        for c in range(ancho):
            fila_nueva.append(" ")
        matriz.append(fila_nueva)

    # Dibujar bordes
    for c in range(ancho):
        matriz[0][c] = "═"
        matriz[alto - 1][c] = "═"
    for f in range(alto):
        matriz[f][0] = "║"
        matriz[f][ancho - 1] = "║"
        
    matriz[0][0] = "╔"
    matriz[0][ancho - 1] = "╗"
    matriz[alto - 1][0] = "╚"
    matriz[alto - 1][ancho - 1] = "╝"

    # Dibujar serpiente
    contador = 0
    for parte in cuerpo_serpiente:
        f = parte[0]
        c = parte[1]
        if f > 0 and f < alto - 1 and c > 0 and c < ancho - 1:
            if contador == 0:
                matriz[f][c] = "●" # Cabeza
            else:
                matriz[f][c] = "○" # Cuerpo
        contador = contador + 1

    # Dibujar obstaculos
    for obs in lista_obstaculos:
        f = obs[0]
        c = obs[1]
        if f > 0 and f < alto - 1 and c > 0 and c < ancho - 1:
            matriz[f][c] = f"{COLORES['AMARILLO']}■{COLORES['RESET']}"

    # Dibujar comida
    f_comida = pos_comida[0]
    c_comida = pos_comida[1]
    matriz[f_comida][c_comida] = f"{COLORES['ROJO']}◆{COLORES['RESET']}"

    # Imprimir todo
    # Mover cursor al inicio (truco para que no parpadee tanto)
    print("\033[H", end="") 
    
    for fila in matriz:
        texto_fila = ""
        for celda in fila:
            if celda == "●" or celda == "○":
                texto_fila = texto_fila + configuracion["color_serpiente"] + celda + COLORES["RESET"]
            else:
                texto_fila = texto_fila + celda
        print(texto_fila)

def iniciar_juego(nivel=1):
    ancho = 40
    alto = 20
    
    # Posicion inicial
    cuerpo = [
        [alto // 2, ancho // 2],
        [alto // 2, ancho // 2 - 1],
        [alto // 2, ancho // 2 - 2],
    ]
    direccion_actual = "derecha"
    proxima_direccion = "derecha"
    
    obstaculos = obtener_obstaculos(nivel)
    velocidad = obtener_velocidad(nivel)
    comida = crear_comida(alto, ancho, cuerpo, obstaculos)
    puntos = 0
    
    limpiar_pantalla()
    
    jugando = True
    while jugando:
        # Leer entrada del usuario
        tecla = leer_tecla()
        if tecla == "salir":
            jugando = False
            return
            
        if tecla:
            # Evitar giro de 180 grados
            if tecla == "arriba" and direccion_actual != "abajo":
                proxima_direccion = "arriba"
            elif tecla == "abajo" and direccion_actual != "arriba":
                proxima_direccion = "abajo"
            elif tecla == "izquierda" and direccion_actual != "derecha":
                proxima_direccion = "izquierda"
            elif tecla == "derecha" and direccion_actual != "izquierda":
                proxima_direccion = "derecha"
        
        direccion_actual = proxima_direccion
        
        # Calcular nueva cabeza
        cabeza = cuerpo[0]
        nueva_cabeza = [cabeza[0], cabeza[1]]
        
        if direccion_actual == "arriba":
            nueva_cabeza[0] = nueva_cabeza[0] - 1
        elif direccion_actual == "abajo":
            nueva_cabeza[0] = nueva_cabeza[0] + 1
        elif direccion_actual == "izquierda":
            nueva_cabeza[1] = nueva_cabeza[1] - 1
        elif direccion_actual == "derecha":
            nueva_cabeza[1] = nueva_cabeza[1] + 1
            
        # Choques con paredes
        if nueva_cabeza[0] == 0 or nueva_cabeza[0] == alto - 1 or \
           nueva_cabeza[1] == 0 or nueva_cabeza[1] == ancho - 1:
            mostrar_fin_juego("Chocaste con la pared", puntos)
            return

        # Choques con sigo misma
        if nueva_cabeza in cuerpo:
            mostrar_fin_juego("Te mordiste a ti mismo", puntos)
            return
            
        # Choques con obstaculos
        choca_obs = False
        for obs in obstaculos:
            if obs[0] == nueva_cabeza[0] and obs[1] == nueva_cabeza[1]:
                choca_obs = True
                break
        if choca_obs:
            mostrar_fin_juego("Chocaste con obstaculo", puntos)
            return
            
        # Mover serpiente
        cuerpo.insert(0, nueva_cabeza)
        
        # Comer
        if nueva_cabeza[0] == comida[0] and nueva_cabeza[1] == comida[1]:
            puntos = puntos + 10
            comida = crear_comida(alto, ancho, cuerpo, obstaculos)
            # Aumentar velocidad un poco
            if velocidad > 0.03:
                velocidad = velocidad - 0.001
        else:
            # Si no come, borrar la cola
            cuerpo.pop()
            
        dibujar(alto, ancho, cuerpo, obstaculos, comida)
        print(f"Puntos: {puntos} - Nivel: {nivel}")
        
        time.sleep(velocidad)
