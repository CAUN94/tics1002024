# El comando input() nos permite pedir información al usuario

# Pedir al usuario un número y mostrarlo
numero = input("Ingrese un número: ")
print("El número ingresado es:", numero)

# Pedir al usuario su nombre y mostrar un saludo
nombre = input("Ingrese su nombre: ")
print("¡Hola,", nombre, "!")

# Pedir al usuario su nombre, apellido y edad y mostrar un mensaje
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
print(f"¡Hola, {nombre} {apellido}! Usted tiene {edad} años.")
# Pero si quiero sumar la edad con 1, no puedo hacerlo directamente porque la función input() devuelve un string
# edad = edad + 1
# Entonces pedimos todos los datos como string y luego convertimos la edad a entero
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
print(f"¡Hola, {nombre} {apellido}! Usted tiene {edad+1} años.")
