# Hasta ahora hemos visto como crear listas, como acceder a sus elementos, como modificarlos, como agregar datos  y a recoorrerlas con un ciclo for.

# Un breve repaso seria:
# Crear una lista:

lista = [1, 2, 3, 4, 5]

# Acceder a un elemento de la lista:

print(lista[0])
print(lista[1])
print(lista[2])

# Modificar un elemento de la lista:

lista[0] = 10
print(lista)

# Agregar un elemento a la lista:

lista.append(6)
lista.append(7)
print(lista)

# Recorrer la lista con un ciclo for:

for elemento in lista:
    print(elemento)

# Tambien podemos recorrer la lista con for y range:

for i in range(len(lista)):
    print(lista[i])

# Ahora veremos como crear listas anidadas o listas de listas.
# Una lista anidada es una lista que contiene otras listas como elementos.
# Por ejemplo, si queremos representar una matriz de 3x3, podemos hacerlo con una lista anidada:

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)

# Para acceder a un elemento de la matriz, primero accedemos a la fila y luego a la columna:

# Primero veamos como acceder a una fila:

print(matriz[0]) # [1, 2, 3]
print(matriz[1]) # [4, 5, 6]
print(matriz[2]) # [7, 8, 9]

# Ahora veamos como acceder a un elemento de la matriz:

print(matriz[0][0]) # 1
print(matriz[0][1]) # 2
print(matriz[0][2]) # 3
print(matriz[1][0]) # 4
print(matriz[1][1]) # 5
print(matriz[1][2]) # 6
print(matriz[2][0]) # 7
print(matriz[2][1]) # 8
print(matriz[2][2]) # 9
