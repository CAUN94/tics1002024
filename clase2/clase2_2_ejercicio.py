# Ejercicio 1: Pida al usuario un numero y vea si es mayor o igual a 18, en caso de serlo imprima "Eres mayor de edad"

# edad = int(input("Edad: "))
# if edad >= 18:
#     print("Eres mayor de edad")
# if edad < 18:
#     print("Eres menor de edad")

# Ejercicio 2: Pida al usuario una contraseña, si esta es "contraseña123" imprima "Contraseña correcta"
    
# contraseña = input('Contraseña: ')
# contraseña_correcta = "contraseña123"

# if contraseña == contraseña_correcta:
#     print("Ingresaste")
# if contraseña != contraseña_correcta:
#     print("No Ingresaste")

# Ejercicio 3: Pida al usuario un numero y si este es par imprima "Es par"
# Recuerde que el comando % retorna el resto de una division
# 5%2 = 1
# 4%2 = 0
# 3%2 = 1
# 2%2 = 0

num = int(input('Numero: '))

if num%2 == 0:
    print(f'{num} es par')
