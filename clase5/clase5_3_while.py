# Sigamos con el while, ahora vamos a hacer un programa que imprima los números del 1 al 10

contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# Una de las ventajas que tiene el ciclo while es poder trabajar usando una condiciones, por lo que podemos hacer lo siguiente
    
# Podemos usar while para trabajar con listas, por lo que podemos hacer lo siguiente
    
lista = [2,5,3,6,1,9,2,10,7,12]
indice = 0
while contador < len(lista):
    print(lista[indice])
    indice += 1

# Aunque en general  es más comun usar while para pedir valores al usuario y guardarlos en una lista, por lo que podemos hacer lo siguiente
    
lista = []
# Agregaremos datos a la lista hasta que el usuario ingrese '-1

while True:
    dato = input('Ingrese un dato o -1 para terminar: ')
    if dato == '-1':
        break
    lista.append(dato)

print(lista)


