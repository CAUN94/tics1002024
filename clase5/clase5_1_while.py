# Vamos a conocer un nuevo ciclo llamado while, este ciclo se ejecuta mientras una condicion sea verdadera, por lo que no necesariamente necesita un rango como el for

# A diferencia de un for puede funcionar de forma indefinida si no se le da una condicion de parada, por lo que se debe tener cuidado al usarlo

# La forma de estrucutra de un while es la siguiente:

# while condicion:

# Igual que con el if, la condicion debe ser verdadera para que el ciclo se ejecute, si la condicion es falsa el ciclo no se ejecutara

while 2 >1:
    print('Esto es verdad')
    break

# Una forma bastante comun de usar el while es con un contador, por lo que se puede hacer lo siguiente

# En este caso el ciclo se ejecutara mientras el contador sea menor a 10, por lo que se imprimira los numeros del 0 al 9

cont = 0
while True:
    print(cont)
    cont = cont+1
    if cont >= 10:
        break
# Una forma de hacer un ciclo infinito es hacer que la condicion siempre sea verdadera, por lo que se puede hacer lo siguiente
    
r = input('Quieres continuar si/no: ')
while r == 'si':
    print('Que bueno')
    r = input('Quieres continuar si/no: ')

# En este caso el ciclo se ejecutara mientras la respuesta sea 'si', si la respuesta es 'no' el ciclo se detendra



    