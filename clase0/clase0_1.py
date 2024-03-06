# El primer programa en Python que cualquier programador debe escribir es el clásico "Hola Mundo". La historia del "Hola Mundo" nace en el libro "The C Programming Language" de Brian Kernighan y Dennis Ritchie, publicado en 1978. En este libro, el primer ejemplo de código es un programa que imprime "Hola Mundo" en la pantalla. Se dice que Steve Wosniak, cofundador de Apple, escribió el primer "Hola Mundo" en el lenguaje de programación BASIC en 1975 para demostrar que los computadores personales podían ser amigables. En Python, el "Hola Mundo" es tan simple como escribir:

print("Hola Mundo")

# Este código imprime "Hola Mundo" en la pantalla. La función print() es una función incorporada de Python que imprime el texto que se le pasa como argumento en la pantalla. El texto que se pasa como argumento debe estar entre comillas dobles o simples. En Python, las comillas dobles y simples son equivalentes.

# Podemos escribir todos los print que queramos

print("Hola de nuevo")

# Si ejecutamos este código, veremos que se imprime "Hola Mundo" y "Hola de nuevo" en la pantalla, notaron que hubo un salto de línea entre las dos impresiones. Esto se debe a que la función print() agrega un salto de línea al final de lo que imprime. 

# Y si ponemos un print sin nada adentro?

print()
print('Otro texto')

# Si ejecutamos este código, veremos que se imprime un salto de línea en la pantalla. Esto se debe a que la función print() imprime un salto de línea si no se le pasa ningún argumento.

# print() es una funcion que requiere de cero o mas argumentos, y siempre imprime un salto de linea al final, a menos que se le pase el argumento end=''
# print('Hola Mundo', end='') Impriimiria "Hola Mundo" sin salto de linea al final
print('Hola Mundo', end='')
print('Otro Hola Mundo', end='-')
print('Hola Mundo de nuevo')




