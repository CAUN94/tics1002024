# Ahora que ya entendemos como se crean las listas anidadas y como acceder a sus elementos, veamos como recorrerlas.

# Para recorrer una lista anidada con un ciclo for, primero recorremos las filas y luego recorremos las columnas de cada fila.

# Partamos con las filas:

# Matriz de 5x5

matriz = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15],[16, 17, 18, 19, 20],[21, 22, 23, 24, 25]]

# Recorremos las filas
for fila in matriz:
    print(fila)

# Ahora que ya tenmos esta información que nos entrega las filas, podemos recorrer las columnas de cada fila.

# Recorremos las filas
for fila in matriz:
    # Recorremos las columnas
    for columna in fila:
        print(columna)

# En este caso, primero recorremos las filas y luego recorremos las columnas de cada fila.

# Ahora muchas veces tendremos que usar las coordenadas de los elementos de la matriz.

# [1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10]
# [11, 12, 13, 14, 15]
# [16, 17, 18, 19, 20]
# [21, 22, 23, 24, 25]

# Por ejemplo, si queremos acceder al elemento de la fila 2 y columna 3, podemos hacerlo de la siguiente manera:

print(matriz[1][2]) # 8

# Nota que la fila 2 corresponde al indice 1 y la columna 3 corresponde al indice 2.

# Otro ejemplo, si queremos acceder al elemento de la fila 4 y columna 5, podemos hacerlo de la siguiente manera:

print(matriz[3][4]) # 20

# Nota que la fila 4 corresponde al indice 3 y la columna 5 corresponde al indice 4.

# Ahora que ya sabemos como recorrer una lista anidada, veamos como modificar un elemento de la matriz.

# Por ejemplo, si queremos modificar el elemento de la fila 3 y columna 4, podemos hacerlo de la siguiente manera:

matriz[2][3] = 100

print(matriz)

# Finalmente recorreremos la matriz con un ciclo for y range.

# Recorremos las filas
for i in range(len(matriz)):
    # Recorremos las columnas
    # Nota que len(matriz[i]) nos entrega la cantidad de columnas de la fila i
    for j in range(len(matriz[i])):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    print()