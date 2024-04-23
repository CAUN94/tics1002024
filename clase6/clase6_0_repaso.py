print('Hola Mundo')
print(2*2)
print(4*'Hola')
a = 2
a = 3
print(a)
b = 4
b = b + a
print(b)

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))

print('Hola', nombre, apellido, 'tienes', edad, 'años')

nr = int(input('Ingrese un numero: '))
if nr % 2 == 0:
    print('El numero', nr, 'es par')
else:
    print('El numero', nr, 'es impar')

lista = [1, 2, 3, 4, 5]
for variable_que_se_me_dio_la_gana in lista:
    print(variable_que_se_me_dio_la_gana)

var = 0
for i in range(100,201):
    var = var + i
print(var)

nr = int(input('Ingrese un numero: '))

cont = 0
for i in range(1, nr+1):
    if nr % i == 0:
        cont = cont + 1

if cont == 2:
    print('El numero', nr, 'es primo')
else:
    print('El numero', nr, 'no es primo')