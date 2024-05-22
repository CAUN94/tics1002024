# Ahora que ya tenemos manejo sobre las listas anidadas vamos a ver algunos conceptos más avanzados sobre las listas bidimensionales.

# Listas bidimensionales, estas se pueden ocupar para marcar cualquier tipo de tablero, como un tablero de ajedrez, un tablero de damas, un tablero de sudoku, entre otros ejemplos.

# En este caso vamos a hacer un tabler de el juego gato, para este necesitamos hacer los siguientes pasos para poder hacer el tablero:

# 1. Crear el tablero con las dimensiones 3x3.
# 2. Imprimir el tablero.
# 3. Pedirle al jugador 1 que ingrese la posición donde quiere marcar.
# 4. Marcar la posición del jugador 1 en el tablero con una X.
# 5. Imprimir el tablero.
# 6. Pedirle al jugador 2 que ingrese la posición donde quiere marcar.
# 7. Marcar la posición del jugador 2 en el tablero con una O.
# 8. Imprimir el tablero.
# 9. Chequear si hay un ganador, si lo hay imprimirlo.
# 10. Si no hay un ganador repetir los pasos 3 al 8.

# En este caso lo haremos sin funciones

# 1. Crear el tablero con las dimensiones 3x3.
tablero = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]

# 2. Imprimir el tablero.
for i in range(len(tablero)):
    print(tablero[i])

juego = True

while juego:
    # 3. Pedirle al jugador 1 que ingrese la posición donde quiere marcar.
    print("Jugador 1")
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    # 4. Marcar la posición del jugador 1 en el tablero con una X.
    tablero[fila][columna] = "X"
    # 5. Imprimir el tablero.
    for i in range(len(tablero)):
        print(tablero[i])

    # 6. Pedirle al jugador 2 que ingrese la posición donde quiere marcar.
    print("Jugador 2")
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    # 7. Marcar la posición del jugador 2 en el tablero con una O.
    tablero[fila][columna] = "O"
    # 8. Imprimir el tablero.
    for i in range(len(tablero)):
        print(tablero[i])

    # 9. Chequear si hay un ganador, si lo hay imprimirlo.
    # Chequeamos si hay un ganador en las filas
    for i in range(len(tablero)):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != 0:
            print(f"El ganador es {tablero[i][0]}")
            juego = False
            break
    # Chequeamos si hay un ganador en las columnas
    for i in range(len(tablero)):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != 0:
            print(f"El ganador es {tablero[0][i]}")
            juego = False
            break
    # Chequeamos si hay un ganador en las diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != 0:
        print(f"El ganador es {tablero[0][0]}")
        juego = False
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != 0:
        print(f"El ganador es {tablero[0][2]}")
        juego = False

    # En caso de que todo el tablero este lleno y no haya un ganador, terminamos el juego
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 0:
                break
        else:
            continue
        print("No hay ganador")
        break

# Mostramos al ganador
print(f"El ganador es {tablero[0][0]}")

