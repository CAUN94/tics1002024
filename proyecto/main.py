import random
from jugada_cpu import jugada_cpu
# CONFIGURACION DEL JUEGO

# Valores que representan las distintas jugadas
VACIO = 0
BLANCO = 1
NEGRO = -1
BLOQUEADO = 2
CPU = NEGRO # Color asignado a la computadora

TAMAÑO = 8 # Tamaño del tablero (8x8 por defecto)
CELDAS_BLOQUEADAS = 8 # Cantidad de celdas a bloquear
RONDAS = 1 # Cantidad de rondas a jugar (Cambiar a 1000 para el reporte final)

# Configuración del despliegue en terminal
MOSTRAR_TERMINAL = True #Mostrar juego en terminal
NOMBRE_COLUMNAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:TAMAÑO]
NOMBRE_FILAS = list(range(1,TAMAÑO + 1))
for i in range(len(NOMBRE_FILAS)):
    NOMBRE_FILAS[i] = str(NOMBRE_FILAS[i])

# Genera un tablero de TAMAÑOxTAMAÑO con CELDAS_BLOQUEADAS cantidad de celdas bloqueadas en lugares aleatorios.
def inicializar_tablero():
    tablero = []
    for _ in range(TAMAÑO):
        fila = []
        for _ in range(TAMAÑO):
            fila.append(VACIO)
        tablero.append(fila)
    for _ in range(CELDAS_BLOQUEADAS):
        fila_aleatoria = random.randint(0,TAMAÑO - 1)
        columna_aleatoria = random.randint(0,TAMAÑO - 1)
        while tablero[fila_aleatoria][columna_aleatoria] != VACIO:
            fila_aleatoria = random.randint(0,TAMAÑO - 1)
            columna_aleatoria = random.randint(0,TAMAÑO - 1)
        else:
            tablero[fila_aleatoria][columna_aleatoria] = BLOQUEADO
    return tablero

# Despliega el tablero en el terminal
def mostrar_tablero(tablero):
    if not MOSTRAR_TERMINAL:
        return
    
    print(f"   {' '.join(NOMBRE_COLUMNAS)}")
    for i, fila in enumerate(tablero):
        mostrar_fila = NOMBRE_FILAS[i]
        if i < 9:
            mostrar_fila+= " |"
        else:
            mostrar_fila+= "|"

        for celda in fila:
            mostrar_celda = " "
            if celda == BLANCO:
                mostrar_celda = "B"
            elif celda == NEGRO:
                mostrar_celda = "N"
            elif celda == BLOQUEADO:
                mostrar_celda = "X"
            mostrar_fila += f"{mostrar_celda}|"
        print(mostrar_fila)

# Revisa la validad de la jugada en base a las reglas del juego (la celda debe estar vacia)
def jugada_es_valida(tablero, fila, columna):
    if tablero[fila][columna] == VACIO :
        return True
    return False

# Genera una lista bidimensional con todas las casillas disponibles donde hay jugadas validas    
def obtener_jugadas_validas(tablero):
    jugadas_validas = []
    for fila in range(TAMAÑO):
        for columna in range(TAMAÑO):
            if jugada_es_valida(tablero, fila, columna):
                jugadas_validas.append([fila, columna])
    return jugadas_validas

# Logíca para cambiar las fichas en base a las reglas del juego (cuando el jugador encierra fichas del oponente entre sus fichas)
def cambiar_fichas(tablero, fila, columna, jugador):
    # Se definen las 8 direcciones donde se pueden cambiar fichas
    direcciones = [
        [-1, -1], [-1, 0], [-1, 1],
        [ 0, -1], [ 0, 0], [ 0, 1],
        [ 1, -1], [ 1, 0], [ 1, 1],
    ]

    oponente = -jugador

    for cambio_fila, cambio_columna in direcciones:
        fila_actual = fila + cambio_fila
        columna_actual = columna + cambio_columna
        fichas_a_cambiar = []

        while 0 <= fila_actual < TAMAÑO and 0 <= columna_actual < TAMAÑO and tablero[fila_actual][columna_actual] == oponente:
            fichas_a_cambiar.append([fila_actual, columna_actual])
            fila_actual += cambio_fila
            columna_actual += cambio_columna

        if 0 <= fila_actual < TAMAÑO and 0 <= columna_actual < TAMAÑO and tablero[fila_actual][columna_actual] == jugador:
            for fila, columna in fichas_a_cambiar:
                tablero[fila][columna] = jugador

# Actualizar el tablero en base a la jugada
def realizar_jugada(tablero, fila, columna, jugador):
    tablero[fila][columna] = jugador
    cambiar_fichas(tablero, fila, columna, jugador)

# Código para jugada de jugador manual con validación
def jugada_jugador_manual(tablero):
    jugada = input("Ingresa tu jugada (por ejemplo: 'D3'): ").strip().upper()
    while len(jugada) not in [2,3] or jugada[0] not in NOMBRE_COLUMNAS or not jugada[1:] in NOMBRE_FILAS or not jugada_es_valida(tablero, NOMBRE_FILAS.index(jugada[1:]), NOMBRE_COLUMNAS.index(jugada[0])):
        print("Jugada Inválida")
        jugada = input("Ingresa tu jugada (por ejemplo: 'D3'): ").strip().upper()
        
    return NOMBRE_FILAS.index(jugada[1:]), NOMBRE_COLUMNAS.index(jugada[0])

def jugada_jugador(tablero):
    # Acá se debe implementar el código a competir.
    return 0,0

# Cálculo de puntajes para el CPU y el jugador (contar el total de fichas de cada uno)
def obtener_resultado(tablero):
    jugador = -CPU
    puntos_cpu = 0
    puntos_jugador = 0
    for fila in tablero:
        puntos_cpu += fila.count(CPU)
        puntos_jugador += fila.count(jugador)

    return puntos_cpu, puntos_jugador

# Guardar resultados en un archivo CSV
def guardar_resultados(resultados, nombre_archivo="resultados.csv"):
    with open(nombre_archivo, mode='w') as archivo:
        archivo.write("Game,Score CPU,Score Jugador,Parte CPU\n")
        for i, resultado in enumerate(resultados):
            archivo.write(f"{i + 1},{resultado[0]},{resultado[1]},{resultado[2]}\n")

# Función para jugar una ronda
def jugar():
    tablero = inicializar_tablero()
    jugador_actual = random.choice([BLANCO, NEGRO])
    parte_cpu = jugador_actual == CPU
    while True:
        mostrar_tablero(tablero)
        jugadas_validas = obtener_jugadas_validas(tablero)
        if not jugadas_validas:
            break

        if jugador_actual == CPU:
            fila, columna = jugada_cpu(tablero)
        else:
            fila, columna = jugada_jugador_manual(tablero) # Reemplazar con jugada_jugador(tablero) una vez implementado.

        realizar_jugada(tablero, fila, columna, jugador_actual)
        jugador_actual = -jugador_actual

    puntos_cpu, puntos_jugador = obtener_resultado(tablero)

    if MOSTRAR_TERMINAL:
        print(f"Puntos Jugador: {puntos_jugador}")
        print(f"Puntos CPU: {puntos_cpu}")
        print(f"Primer Turno: {'CPU' if parte_cpu else 'Jugador'}")
        if puntos_jugador > puntos_cpu:
            print("Felicitaciones Jugador Gana!")
        elif puntos_jugador < puntos_cpu:
            print("CPU Gana!")
        else:
            print("Es un empate!")
    
    return puntos_cpu, puntos_jugador, parte_cpu


resultados = []
for _ in range(RONDAS):
    resultados.append(jugar())
guardar_resultados(resultados)