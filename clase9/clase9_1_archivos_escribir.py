# Además de leer tambien podemos escribir en archivos, para esto debemos abrir el archivo en modo escritura, para esto se usa el parametro 'w' en el metodo open, si el archivo no existe se creara uno nuevo, si ya existe se sobreescribira.

# En este caso quiero crear un archivo nuevo llamado archivo2.txt y escribir la siguiente informacion en el: Cristobal,Ugarte,Nuñez

archivo = open('clase9/archivo2.txt', 'w')

archivo.write('Cristobal,Ugarte,Nuñez\n')

archivo.close()

# Ahora podemos hacer esto mismo para muchos datos

archivo = open('clase9/archivo2.txt', 'w')
archivo.write('Cristobal,Ugarte,Nuñez\n')
archivo.write('Juan,Perez,Lopez\n')
archivo.write('Pedro,Perez,Lopez\n')

archivo.close()

# Notese que el archivo se sobreescribe cada vez que se abre en modo escritura.

# Ahora llenemos el archivo con datos de una encuesta

archivo = open('clase9/archivo2.txt', 'w')

archivo.write('Nombre,Apellido,Edad,Sexo\n')

while True:
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    edad = input('Ingrese su edad: ')
    sexo = input('Ingrese su sexo: ')
    
    archivo.write(f'{nombre},{apellido},{edad},{sexo}')
    # Agregamos el salto de linea para que la siguiente persona se escriba en la siguiente linea
    archivo.write('\n')
    # Preguntamos si quiere seguir ingresando datos
    continuar = input('Desea seguir ingresando datos? (si/no): ')
    if continuar == 'no':
        break
# Finalmente podemos hacer lo mismo desde una matriz

archivo = open('clase9/archivo2.txt', 'w')

matriz = [
    ['Cristobal', 'Ugarte', 'Nuñez'], 
    ['Juan', 'Perez', 'Lopez'], 
    ['Pedro', 'Perez', 'Lopez']
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        archivo.write(matriz[i][j])
        if j < len(matriz[i]) - 1:
            archivo.write(',')
    archivo.write('\n')

