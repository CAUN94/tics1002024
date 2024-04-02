# Ahora que ya tenemos una idea de como funcionan las listas, vamos a ver sus funciones con más detalle.

# Primero podemos crear una lista con distintos tipos de datos

lista = [1,2,33,"Hola",5.5]

# Pero estos datos son aletorios, la idea es que igual que con las variables, las listas tengan un proposito, por lo que podemos crear una lista con los datos de un alumno

# Nombre,Apellido,Nota1,Nota2,Nota3,Porcentaje de asistencia

alumno1 = ["Juan","Delgado",5.5,6.0,4.5,60]

# Ahora, si queremos acceder a un elemento de la lista, podemos hacerlo de la siguiente manera:

print(f"{alumno1[0]} {alumno1[1]} promedio de notas: {(alumno1[2]+alumno1[3]+alumno1[4])/3}, su asitencia es del {alumno1[5]}%")

# Las listas parte en 0, pero si queremos acceder al ultimo elemento de la lista, podemos hacerlo de la siguiente manera:

lista = [1,2,3,4,5]
# print(lista[-5])

# Como podemos ver, si ponemos un indice negativo, python empieza a contar desde el final de la lista, por lo que -1 es el ultimo elemento de la lista, -2 es el penultimo, y asi sucesivamente.

# Además de lo que ya vimos podemos obtener informacion de la lista mediante las siguientes funciones:

# len(lista): Nos entrega la cantidad de elementos que tiene la lista

lista = [1,3,5,"Hola",7,9.8,10,12,'Chao']
print(len(lista))

# Esto sirve para saber cuantos elementos tiene una lista, lo que nos puede servir para saber cuantas veces tenemos que iterar sobre una lista, o para saber si una lista esta vacia.

# Ahora muchas veces la lista solo va a tener datos numericos, por lo que podemos hacer operaciones con la lista, como sumar todos los elementos de la lista.


# sum(lista): Nos entrega la suma de todos los elementos de la lista

# Esto solo funciona si todos los elementos de la lista son numeros, si hay un elemento que no es un numero, nos dara un error.

lista = [-50,1,2,3,4,5,20]

# max(lista): Nos entrega el elemento mas grande de la lista
# min(lista): Nos entrega el elemento mas pequeño de la lista

print(sum(lista))
print(max(lista))
print(min(lista))


