# Otros ejercicios clasicos con matrices son en los que deben revisar el contenido que al rededor de una coordenada, por ejemplo:

# 1. Dada una matriz de dimensiones nxm y una coordenada (x, y), retorne el contenido de la coordenada y la suma de los elementos al rededor de la coordenada.

import random

def crear_matriz(n, m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(random.randint(0, 10))
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

n = 5
m = 6

matriz = crear_matriz(n, m)
mostrar_matriz(matriz)

while True:
    # le pedimos un coordenada al usuario
    x = int(input("Ingrese la coordenada x: "))
    y = int(input("Ingrese la coordenada y: "))

    # chequeamos que la coordenada este dentro de los limites de la matriz
    if x < 0 or x >= n or y < 0 or y >= m:
        print("Coordenada fuera de los limites de la matriz")
    else: 
        break

# mostramos el contenido de la coordenada
print(f"El contenido de la coordenada ({x}, {y}) es {matriz[x][y]}")

# Mostramos los valores que estan al rededor de la coordenada

suma = 0
for i in range(x-1, x+2):
    for j in range(y-1, y+2):
        if i >= 0 and i < n and j >= 0 and j < m:
            if i == x and j == y:
                continue
            print(f"El contenido de la coordenada ({i}, {j}) es {matriz[i][j]}")
            suma += matriz[i][j]

# mostramos la suma de los elementos al rededor de la coordenada

print(f"La suma de los elementos al rededor de la coordenada ({x}, {y}) es {suma}")










        
    