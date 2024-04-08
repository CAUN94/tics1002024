# La semana pasada vimos las listas y sus funciones basicas que nos permiten agregar, quitar y modificar elementos.

# Creamos una lista vacia

lista = []

# Agregamos elementos a la lista

lista.append(1)
lista.append(2)
lista.append(3)

# Imprimimos la lista

print(lista) # [1, 2, 3]

# Modificamos un elemento de la lista

lista[0] = 4

# Imprimimos la lista

print(lista) # [4, 2, 3]

# Eliminamos un elemento de la lista

lista.pop(1)

# Imprimimos la lista

print(lista) # [4, 3]

# Insertamos un valor en una posicion especifica

lista.insert(1, 2)

# Imprimimos la lista

print(lista) # [4, 2, 3]

# Eliminamos el ultimo valor de la lista

lista.pop()

# Imprimimos la lista

print(lista) # [4, 2]

# Sumamoos los valores de la lista (Solo funciona si los valores son numericos)

print(sum(lista)) # 6

# Contamos los elementos de la lista

print(len(lista)) # 2

# Obtenemos el maximo valor de la lista

print(max(lista)) # 4

# Obtenemos el minimo valor de la lista

print(min(lista)) # 2
