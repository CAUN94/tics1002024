# Como ya hemos visto hasta ahora hay muchos casos en los que nos serviria trabajar con una lista de forma dinamica, es decir, poder usar todos los valores de una lista sin tener que escribirlos uno por uno.

# En python podemos hacer esto con un ciclo for, que nos permite recorrer todos los valores de una lista uno por uno.

# El comando for se construye de la siguiente manera

# for valor in lista:
    # print(valor)

# for es una palabra reservada que nos indica que vamos a hacer un ciclo
# valor es una variable que nosotros inventamos, que va a tomar el valor de cada elemento de la lista uno por uno
# in es una palabra reservada que nos indica que vamos a recorrer los elementos de la lista
# lista es la lista que vamos a recorrer
# : es una parte fundamental del ciclo, indica que lo que sigue es el bloque de codigo que se va a ejecutar en cada iteracion del ciclo
# e igual que con los if se debe indentar el bloque de codigo que se va a ejecutar en cada iteracion del ciclo


# Veamos un ejemplo

lista = [1, 2, 3, 4, 5]

for valor in lista:
    print(valor)

# 1
# 2
# 3
# 4
# 5

# En este caso la variable valor toma el valor de cada elemento de la lista uno por uno y lo imprime y esto funciona para cualquier lista

lista2 = [10, 'Hola', 3.14, 'Javier', 5]

for valor in lista2:
    print(valor)

# 10
# Hola
# 3.14
# Javier
# 5

# Y recordemos que los strings pueden usarse como listas

string = 'Hola Mundo'

for letra in string:
    print(letra)

# H
# o
# l
# a
#
# M
# u
# n
# d
# o

# En este caso la variable letra toma el valor de cada letra de la palabra 'Hola Mundo' uno por uno y lo imprime

# Ahora cuando son listas numericas muy grandes, se dificulta crear la lista, por lo que podemos usar range para crearla y recorrerla al mismo tiempo

for valor in range(100):
    print(valor)

# Eso imprimiria los numeros del 0 al 99

# Algo importane a considerar es que no es necesario que la variable que recorre la lista se llame valor, puede llamarse como querramos y además tampoco es necesaria usarla

for i in range(10):
    print('Hola')

    
