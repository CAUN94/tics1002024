# Como hemos mencionado las variables pueden almacenar casi cualquier tipo de dato, hoy vamos a ver un tipo de dato que nos permite almacenar varios valores en una sola variable, las listas.

# Partamos con el siguiente problema, tengo que guardar en variables la informacion de 3 alumnos y sus respectivas 3 pruebas del semestre, esto se puede hacer de la siguiente manera:

alumno1 = "Juan"
alumno2 = "Pedro"
alumno3 = "Maria"

nota1_alumno1 = 5.5
nota2_alumno1 = 6.0
nota3_alumno1 = 4.5

nota1_alumno2 = 4.0
nota2_alumno2 = 4.5
nota3_alumno2 = 3.9

nota1_alumno3 = 6.0
nota2_alumno3 = 6.0
nota3_alumno3 = 5.9

# Como podemos ver, esto se puede hacer, pero es muy poco eficiente, ya que estamos repitiendo mucho codigo, y si tuvieramos que agregar mas alumnos, tendriamos que seguir repitiendo codigo, lo que no es una buena practica.

# Para esto es que se crean las listas, las listas son un tipo de dato que nos permite almacenar varios valores en una sola variable, y acceder a ellos de manera mas facil.

# Para crear una lista, se hace de la siguiente manera:

lista_ejemplo = [1, 2, 3, 4, 5]

# Como podemos ver, una lista se crea poniendo los valores que queremos almacenar entre corchetes, y separandolos por comas, cada valor en la lista se le llama elemento.

# Cada elemento de la lista tiene un indice, que es la posicion que ocupa en la lista, los indices en python empiezan en 0, por lo que el primer elemento de la lista tiene indice 0, el segundo elemento tiene indice 1, y asi sucesivamente.

# Para acceder a un elemento de la lista, se hace de la siguiente manera:

print(lista_ejemplo[0]) # 1
print(lista_ejemplo[1]) # 2
print(lista_ejemplo[2]) # 3
print(lista_ejemplo[3]) # 4
print(lista_ejemplo[4]) # 5
print(lista_ejemplo[5]) # IndexError: list index out of range, ya que no existe un elemento en la posicion 5

# Como podemos ver, para acceder a un elemento de la lista, se pone el nombre de la lista, seguido de corchetes, y dentro de los corchetes el indice del elemento que queremos acceder.

# Ahora, volviendo al problema anterior, podemos guardar la informacion de los alumnos y sus notas en listas de la siguiente manera:

alumnos = ["Juan", "Pedro", "Maria"]
notas1_alumnos = [5.5, 4.0, 6.0]
notas2_alumnos = [6.0, 4.5, 6.0]
notas3_alumnos = [4.5, 3.9, 5.9]

# Como podemos ver, ahora tenemos una lista para los nombres de los alumnos, y una lista para cada prueba, en donde cada elemento de la lista corresponde a la nota de un alumno en esa prueba.

# Ahora, si queremos acceder a la informacion de un alumno en especifico, podemos hacerlo de la siguiente manera:

print(alumnos[0]) # Juan
print(notas1_alumnos[0]) # 5.5
print(notas2_alumnos[0]) # 6.0
print(notas3_alumnos[0]) # 4.5

