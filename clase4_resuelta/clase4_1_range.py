# En muchas ocaciones nos tocara trabajar con listas que vayan desde un valor inicial hasta un valor final.

# Por ejemplo una lista que vaya del 1 al 10.
# O una lista que vaya del 10 al 25
# O una lista que vaya del 100 al 20
# O una lista que vaya del 0 al 10 aumentando de 2 en 2

# Como todos estos casos son muy largos y tediosos de escribir, python nos provee de una funcion llamada range que nos permite generar listas de una manera mas sencilla.

# La funcion range puede tener de uno a tres argumentos. 
# range(inicio, fin, paso)

# Veamos que pasa si usamos range con un solo argumento

lista1 = range(10)
print(lista1) # range(0, 10)
# Notamos que el resultado no es una lista, sino un objeto de tipo range, para poder convertirlo a una lista debemos usar la funcion list

print(list(lista1)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Como pedimos que tuviera 10 datos, python nos genero una lista que va desde el 0 hasta el 9

# Si usamos dos argumentos, el primer argumento sera el inicio y el segundo sera el fin

lista2 = range(10, 20)
print(list(lista2)) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# En este caso el inicio es 10 y el fin es 20, pero el 20 no se incluye en la lista, es decir, la lista va desde el 10 hasta el 19
# Si quisieramos que la lista fuera del 10 al 20, debemos poner 21 como segundo argumento

lista3 = range(10, 21)
print(list(lista3)) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Si usamos tres argumentos, el primer argumento sera el inicio, el segundo sera el fin y el tercero sera el paso

lista4 = range(0, 10, 2) 
print(list(lista4)) # [0, 2, 4, 6, 8]

# En este caso la lista va desde el 0 hasta el 9 aumentando de 2 en 2, notemos que cuando la suma es mayor o igual al fin, el valor no se incluye en la lista

# Si quisieramos que la lista fuera del 0 al 10 aumentando de 2 en 2, debemos poner 11 como segundo argumento

lista5 = range(0, 11, 2)
print(list(lista5)) # [0, 2, 4, 6, 8, 10]

# Ahora que sabemos esto poodemos hacer la misma lista que hicimos, pero en retroceso

lista6 = range(10, 0, -1)
print(list(lista6)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# En este caso la lista va desde el 10 hasta el 1 disminuyendo de 1 en 1 y estamos obligados a poner -1 (u otro valor) como tercer argumento

