# Hasta ahora hemos trabajado con listas que ya estan creadas, pero tambien podemos crear listas vacias y agregar elementos a la lista, esto se hace de la siguiente manera:

# Creamos una lista vacia
lista = []

# Agregamos elementos a la lista con la funcion append
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)

print(lista) # [1, 2, 3, 4]

# Como podemos ver, para agregar elementos a una lista, se llama a la funcion append de la lista, y se le pasa el elemento que queremos agregar, es importante notar que la funcion append no retorna nada, por lo que no podemos guardar el resultado de la funcion append en una variable.
# Además notar que el elemento se agrega al final de la lista.

# En caso de que queramos agregar un valor en una posicion especifica de la lista, podemos usar la funcion insert, que nos permite agregar un elemento en una posicion especifica de la lista.

# Creamos una lista
lista = [1, 2, 3, 4]

# insert(i, elemento): Agrega el elemento en la posicion i de la lista
lista.insert(2, 5) # Agregamos el numero 5 en la posicion 2
print(lista) # [1, 2, 5, 3, 4]

# Notar que los elementos de la lista se reordenan despues de agregar un elemento en una posicion especifica, por lo que el elemento que estaba en la posicion 2, ahora esta en la posicion 3.

# Muchas veces nos vamos a equivocar al agregar un elemento a una lista, o vamos a querer eliminar un elemento de la lista, para esto podemos usar la funcion pop, que nos permite eliminar un elemento de la lista en una posicion especifica.

# Creamos una lista
lista = [1, 2, 3, 4, 5]

# pop(i): Elimina el elemento en la posicion i de la lista

print(lista) # [1, 2, 3, 4, 5]
lista.pop(2) # Eliminamos el elemento en la posicion 2
print(lista) # [1, 2, 4, 5]

# Notese que los elementos de la lista se reordenan despues de eliminar un elemento, por lo que el elemento que estaba en la posicion 3, ahora esta en la posicion 2.

# En caso de que no se entregue un indice a la funcion pop, se eliminara el ultimo elemento de la lista.
print(lista) # [1, 2, 4, 5]
lista.pop() # Eliminamos el ultimo elemento de la lista
print(lista) # [1, 2, 4]

# Para encontrar la posicion de un elemento en una lista, podemos usar la funcion index, que nos retorna la posicion del primer elemento que coincida con el elemento entregado.

# Creamos una lista
lista  = ['Juan', 'Pedro', 'Diego', 'Juan', 'Pedro']

# index(elemento): Retorna la posicion del primer elemento que coincida con el elemento entregado
print(lista.index('Juan')) # 0
print(lista.index('Pedro')) # 1
