# Vamos a conocer un nuevo ciclo llamado while, este ciclo se ejecuta mientras una condicion sea verdadera, por lo que no necesariamente necesita un rango como el for

# A diferencia de un for puede funcionar de forma indefinida si no se le da una condicion de parada, por lo que se debe tener cuidado al usarlo

# La forma de estrucutra de un while es la siguiente:

# while condicion:

while True:
    print('Este es un ciclo infinito')
    break # Este break es necesario para que el ciclo no sea infinito

# Igual que con el if, la condicion debe ser verdadera para que el ciclo se ejecute, si la condicion es falsa el ciclo no se ejecutara

while False:
    print('Este es un ciclo infinito')

respuesta = 'ni'
while  respuesta == 'si':
    respuesta = input('Desea continuar? si/no: ')
print('Fin del ciclo')

# Una forma bastante comun de usar el while es con un contador, por lo que se puede hacer lo siguiente

contador = 0
while contador < 10:
    print(contador)
    contador += 1

# En este caso el ciclo se ejecutara mientras el contador sea menor a 10, por lo que se imprimira los numeros del 0 al 9
    
# Una forma de hacer un ciclo infinito es hacer que la condicion siempre sea verdadera, por lo que se puede hacer lo siguiente
    
while True:
    print('Este es un ciclo infinito')
    respuesta = input('Desea continuar? si/no: ')
    if respuesta == 'no':
        break

# En este caso el ciclo se ejecutara mientras la respuesta sea 'si', si la respuesta es 'no' el ciclo se detendra



    