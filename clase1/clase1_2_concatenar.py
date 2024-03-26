# Poner print() sin información puede ser ambiguo por lo que es recomendable poner concatenar con un string para que sea mas claro

print('Hoola Mundo')

# Concatenar es unir dos o mas strings o variables o numeros

print("Hola"+"Mundo")

# Tambien lo podemos hacer con comas
print("Hoola","Mundo")

# En este caso no es necesario convertir la variable edad a string, porque la función print() lo hace por nosotros y ademas añade un espacio entre cada argumento

print("Hola",2,"chao",17)

# Mi version favorita es usando f-strings

nombre = "Tommy"
apellido = "Shelby"
edad = 30
print(nombre,apellido,"edad:",edad+1)

# En este caso no es necesario convertir la variable edad a string, porque las f-strings lo hacen por nosotros
# Se agrega una f al principio de las comillas y se pueden poner las variables entre llaves, incluso se pueden hacer operaciones matematicas

print(f"Nombre: {nombre} Apellido: {apellido} Edad:{edad+17}")
