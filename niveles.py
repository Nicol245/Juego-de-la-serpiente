def obtener_obstaculos(nivel):
    # Lista de obstaculos (fila, columna)
    obstaculos = []
    
    if nivel == 1:
        obstaculos = [
            (4, 10), (5, 10), (6, 10), (7, 10),
            (12, 28), (13, 28), (14, 28)
        ]
    
    elif nivel == 2:
        obstaculos = [
            (4, 10), (5, 10), (6, 10), (7, 10),
            (12, 28), (13, 28), (14, 28),
            (9, 16), (9, 17), (9, 18), (9, 19),
            (2, 22), (3, 22), (4, 22), (5, 22)
        ]
        
    elif nivel == 3:
        obstaculos = [
            (4, 10), (5, 10), (6, 10), (7, 10),
            (12, 28), (13, 28), (14, 28),
            (9, 16), (9, 17), (9, 18), (9, 19),
            (2, 22), (3, 22), (4, 22), (5, 22),
            (15, 6), (15, 7), (15, 8), (15, 9), (15, 10),
            (6, 32), (7, 32), (8, 32), (9, 32), (10, 32),
            (3, 30), (3, 31), (3, 32), (3, 33)
        ]
        
    return obstaculos

def obtener_velocidad(nivel):
    # Entre mas bajo el numero, mas rapido
    if nivel == 1:
        return 0.12
    if nivel == 2:
        return 0.09
    if nivel == 3:
        return 0.06
    return 0.12
