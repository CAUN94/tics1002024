# Poner print() sin información puede ser ambiguo por lo que es recomendable poner concatenar con un string para que sea mas claro

# Concatenar es unir dos o mas strings o variables o numeros

nombre = "Tommy"
apellido = "Shelby"
print(nombre + " " + apellido)

edad = 30
# print("Tommy tiene " + edad + " años") , esto devuelve error
print("Tommy tiene " + str(edad) + " años")

# Tambien lo podemos hacer con comas
print("Tommy tiene", edad, "años") 
# En este caso no es necesario convertir la variable edad a string, porque la función print() lo hace por nosotros y ademas añade un espacio entre cada argumento

# Mi version favorita es usando f-strings

print(f"{nombre} tiene {edad} años")
# En este caso no es necesario convertir la variable edad a string, porque las f-strings lo hacen por nosotros
# Se agrega una f al principio de las comillas y se pueden poner las variables entre llaves, incluso se pueden hacer operaciones matematicas

edad = 30
print(f"El año que viene Tommy tendra {edad + 1} años")

