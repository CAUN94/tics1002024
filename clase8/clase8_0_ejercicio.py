# Use la siguiente matriz y haga los siguientes ejercicios:

matriz = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15],[16, 17, 18, 19, 20],[21, 22, 23, 24, 25]]

# 1. Calcula la suma de los elementos de la matriz.

suma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        suma += matriz[i][j]
print(suma)

# Resultado: 325

# 2. Calcula la suma de los elementos de cada fila y los guarde en una lista

fila = []

for i in range(len(matriz)):
    suma = 0
    for j in range(len(matriz[i])):
        suma += matriz[i][j]
    fila.append(suma)

print(fila)

# Resultado: [15, 40, 65, 90, 115]

# 3. Calcula la suma de los elementos de cada columna y los guarde en una lista

columna = []

for i in range(len(matriz[0])):
    suma = 0
    for j in range(len(matriz)):
        suma += matriz[j][i]
    columna.append(suma)

print(columna)

# Resultado: [55, 60, 65, 70, 75]

# 4. Calcula la suma de los elementos de la diagonal principal (1,1) (2,2) ... (n,n)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            suma += matriz[i][j]

print(suma)

# Resultado: 65


