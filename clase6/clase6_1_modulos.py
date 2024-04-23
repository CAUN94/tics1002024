# Carga los modulos tima, math y random
import time
import math
import random

# Imprime la fecha y hora actual
print(time.asctime())

# Haz una pregunta y ve cuanto se demora el usuario en responder
inicio = time.time()
input("Presiona enter para continuar")
final = time.time()
print('Te demoraste', final - inicio, 'segundos')

# Calcula el seno y coseno de un angulo entregado por el usuario
angulo = float(input('Ingrese un angulo: '))
seno = math.sin(angulo)
coseno = math.cos(angulo)
print('El seno de', angulo, 'es', seno)

# Genera un numer aleatorio entre 1 y 100

numero = random.randint(1, 100)
print('El numero aleatorio es', numero)



