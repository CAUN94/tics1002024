import math
import time
import random

# Calcula el seno y coseno de un angulo entregado por el usuario

# angulo = float(input('Ingrese un angulo: '))
# seno = math.sin(angulo)
# coseno = math.cos(angulo)
# print('El seno de', angulo, 'es', seno)
# print('El coseno de', angulo, 'es', coseno)

# Imprime la fecha y hora actual
# print(time.asctime())

# inicio = time.time()
# a = input('Presiona enter para continuar')
# final = time.time()
# print('Te demoraste', int(final - inicio), 'segundos')

# Dame un numero aleatorio 

# print(random.random())

# while hasta que randomo me de un numero igual a 1

inicio = time.time()
nr = random.randint(118, 2740000)
while nr != 200:
    print(nr)
    nr = random.randint(118, 2740000)
final = time.time()
print('Te demoraste', int(final - inicio), 'segundos')