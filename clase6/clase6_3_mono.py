# Creame un codigo con una lista que tenga el abecedario en minuscula y vaya escribiendo letras de forma aleatoria y concatenandolas hasta que genere la palabra 'hola'

import random
import time

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


palabra = ''
palabra_buscada = 'hola'
inicio = time.time()
# la palabra hola debe existir en alguna parte, no necesariamente que sea la ultima palabra
while palabra_buscada not in palabra:
    letra = random.choice(abc)
    palabra = palabra + letra
    print(palabra)
final = time.time()
print()
print('Te demoraste', int(final - inicio), 'segundos')