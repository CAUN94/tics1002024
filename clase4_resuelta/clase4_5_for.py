# El comando for sirve para distintos tipos de funciones, algunas que ya hemos visto incorporadas en python como por ejemplo sum(lista)

lista = [1, 2, 3, 4, 5]

suma = 0
for i in lista:
    suma = suma + i
print(suma)

# También podemoos ir viendo como esta suma va creciendo
# En este caso con un range para trabajar con más datos

for i in range(10,30):
    suma = suma + i
    print(suma)

# Taambién podemos crear una funcion que dinamicamente le pida información al usuario y la guarde en una lista

nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
cantidad_notas = int(input('Cuantas notas desea ingresar: '))

notas = []
for i in range(cantidad_notas):
    nota = float(input('Ingrese la nota: '))
    notas.append(nota)

print('Promedio',(sum(notas)/len(notas)))