# Muchas veces nos toca reutilizar codigo, por lo que es una buena practica encapsular el codigo en funciones.

# Una función es un bloque de código que solo se ejecuta cuando se llama. Puede pasar datos, conocidos como parámetros, a una función. Una función puede devolver datos como resultado.

# Para definir una función en Python, usamos la palabra clave def, seguida del nombre de la función y los paréntesis (). Luego, agregamos dos puntos : y el bloque de código que queremos encapsular en la función.

# Ejemplo de una función que suma dos números:

def suma(a, b):
    # La función suma recibe dos parametros a y b y retorna la suma de ambos.
    return a + b

# Llamamos a la función suma con los valores 5 y 3 y guardamos el resultado en la variable resultado.

resultado = suma(5, 3)

# Imprimimos el resultado.

print(resultado)

# Cosas a tener en cuenta:
# - Las funciones pueden tener parámetros.
# - Las funciones pueden devolver valores con la palabra clave return.
# - Las funciones se definen con la palabra clave def.
# - Las funciones se llaman con el nombre de la función seguido de paréntesis y los argumentos.
# - Las funciones pueden mostrar un mensaje con la palabra clave print.

# Hagamos algunas funciones de ejemplo

# Función que recibe un número y retorna el cuadrado de ese número.

def cuadrado(numero):
    return numero ** 2

# Llamamos a la función cuadrado con el valor 5 y guardamos el resultado en la variable resultado.

resultado = cuadrado(5)
resultado = cuadrado(7)
resultado = cuadrado(9)
resultado = cuadrado(14)

# Función que le hace un cuestionario al usuario y retorna el resultado.

def cuestionario():
    # Preguntamos al usuario su nombre.
    nombre = input("Cual es tu nombre? ")
    # Preguntamos al usuario su edad.
    edad = int(input("Cual es tu edad? "))
    # Preguntamos al usuario si le gusta la programación.
    programacion = input("Te gusta la programación? (si/no) ")
    # Retornamos el nombre, la edad y si le gusta la programación.
    return [nombre, edad, programacion]

cuestionario1 = cuestionario()
cuestionario2 = cuestionario()
cuestionario3 = cuestionario()

# Imprimimos los resultados.
print(cuestionario1)
print(cuestionario2)
print(cuestionario3)

# Función que recibe una lista y retorna la suma de los elementos de la lista.

def suma_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

# Llamamos a la función suma_lista con la lista [1, 2, 3, 4, 5] y guardamos el resultado en la variable resultado.

resultado = suma_lista([1, 2, 3, 4, 5])

# Cree una función que reciba 2 dimensiones y retorne una matriz de dimensiones nxm con todos los elementos en 0.

def matriz_ceros(n, m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(0)
        matriz.append(fila)
    return matriz

# Llamamos a la función matriz_ceros con las dimensiones 3x4 y guardamos el resultado en la variable resultado.

resultado = matriz_ceros(3, 4)

# Imprimimos el resultado.

print(resultado)