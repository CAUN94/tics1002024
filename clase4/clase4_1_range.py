# En muchas ocaciones nos tocara trabajar con listas que vayan desde un valor inicial hasta un valor final.

# Por ejemplo una lista que vaya del 1 al 10.
# O una lista que vaya del 10 al 25
# O una lista que vaya del 100 al 20
# O una lista que vaya del 0 al 10 aumentando de 2 en 2

# Como todos estos casos son muy largos y tediosos de escribir, python nos provee de una funcion llamada range que nos permite generar listas de una manera mas sencilla.

# La funcion range puede tener de uno a tres argumentos. 
# range(inicio, fin, paso)

# Veamos que pasa si usamos range con un solo argumento

# Notamos que el resultado no es una lista, sino un objeto de tipo range, para poder convertirlo a una lista debemos usar la funcion list


# Como pedimos que tuviera 10 datos, python nos genero una lista que va desde el 0 hasta el 9

# Si usamos dos argumentos, el primer argumento sera el inicio y el segundo sera el fin


# En este caso el inicio es 10 y el fin es 20, pero el 20 no se incluye en la lista, es decir, la lista va desde el 10 hasta el 19
# Si quisieramos que la lista fuera del 10 al 20, debemos poner 21 como segundo argumento

# Si usamos tres argumentos, el primer argumento sera el inicio, el segundo sera el fin y el tercero sera el paso


# En este caso la lista va desde el 0 hasta el 9 aumentando de 2 en 2, notemos que cuando la suma es mayor o igual al fin, el valor no se incluye en la lista

# Si quisieramos que la lista fuera del 0 al 10 aumentando de 2 en 2, debemos poner 11 como segundo argumento


# Ahora que sabemos esto poodemos hacer la misma lista que hicimos, pero en retroceso


# En este caso la lista va desde el 10 hasta el 1 disminuyendo de 1 en 1 y estamos obligados a poner -1 (u otro valor) como tercer argumento

