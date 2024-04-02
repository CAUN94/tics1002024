# En el mundo de la programación es muy comun tener que encryptar y desencryptar mensajes, un ejemplo clasico es la utilizacion del codigo morse, que es un sistema de codificacion de texto en el que se representan cada letra del alfabeto, cada numero mediante una secuencia particular de puntos y rayas.

# Cree un programa que le pida al usuario un mensaje y luego le muestre el mensaje encryptado en codigo morse.

# Para esto le entregararemos una lista con el codigo morse de cada letra del alfabeto, numeros .
morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]
# Esto equivale a la lista ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Ejemplo:
# Ingrese un mensaje: mejor  (asuma que el usuario ingreso el mensaje en minusculas y que es de exacatamente 5 caracteres)
# El mensaje encryptado es: --/./.---/---/.-. (en este caso separaremos cada letra con un /)

# Hint
# Use la funcion index para encontrar la posicion de una letra en la lista morse



