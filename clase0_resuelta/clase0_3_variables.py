# Variables
# Las variables son espacios de memoria que se utilizan para almacenar valores, como números, texto, listas, etc.
# Uno asigna el nombre que quiera a la variable y luego le asigna un valor.
# Siempre debe escribirse el nombre de la variable a la izquierda y el valor a la derecha.
# nombre = "valor"
# nombre = 2

nombre = "Tommy"
print(nombre)

# Podemos cambiar el valor de la variable

nombre = "Arthur"
print(nombre)

# Y que pasa si cambio el valor de la variable y luego la imprimo?

nombre = "Arthur"
nombre = "Tommy"

print(nombre)

# Se imprime el ultimo valor que se le asigno a la variable

# Y si lo cambio por un numero?

nombre = "John"
nombre = 2

print(nombre)

# No hay problema, pero no es recomendable, porque puede confundir a otros programadores o a uno mismo

edad = 30

print(edad)

edad = 35

print(edad)

# Como puedo aumentar un valor de una variable?

edad = 30
edad = edad + 5

print(edad)

# Otra forma de hacerlo es con el operador +=

edad = 30
edad += 5

print(edad)

# Y esto puede ser con cualquier operador aritmetico

edad = 30
edad -= 5
print(edad)
edad *= 5
print(edad)
edad /= 5
print(edad)

# En resumen podemos hacer operaciones matematicas con variables y cambiar el valor de las variables

nombre = "Tommy"
apellido = "Shelby"
edad = 30
print(nombre)
print(apellido)
print(edad)

# Y si Tommy cumple años?

edad = edad + 1
print(edad)