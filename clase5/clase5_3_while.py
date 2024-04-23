# Sigamos con el while, ahora vamos a hacer un programa que imprima los números del 1 al 10

# Una de las ventajas que tiene el ciclo while es poder trabajar usando una condiciones, por lo que podemos hacer lo siguiente
    
# Podemos usar while para trabajar con listas, por lo que podemos hacer lo siguiente

lista = [2,4,1,7]
i = 0
while i < len(lista):
    print(lista[i])
    i = i +1

# Aunque en general  es más comun usar while para pedir valores al usuario y guardarlos en una lista, por lo que podemos hacer lo siguiente

# Agregaremos datos a la lista hasta que el usuario ingrese '-1

lista = []
while True:
    valor = int(input('Valor: '))
    lista.append(valor)
    if valor == -1:
        break
print(lista)