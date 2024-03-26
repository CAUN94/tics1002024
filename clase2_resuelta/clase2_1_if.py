# Clase 2: Hoy aprenderemos de comandos de flujos, especificamente los comando if,elif y else

# Partiremos usando los comandos if, que sirven para evaluar si una condición es verdadera o falsa

# Ejemplo 1:
if 5 > 3:
    print("5 es mayor que 3")
    # Notemos que el print() está indentado, esto es importante, ya que python usa la indentación para saber que está dentro del if

# Ejemplo 2:
if 5 < 3:
    print("5 es menor que 3")
    print('Este print no se ejecutará')

if 5 > 3:
    print("5 es mayor que 3")
    print('Este print si se ejecutará')
print('Esto está fuera del if')

# Los otros comandos para comparar son:
# == : Igualdad
# != : Diferencia
# >= : Mayor o igual
# <= : Menor o igual
# > : Mayor
# < : Menor

if 5 == 5:
    print("5 es igual a 5")

if 5 != 3:
    print("5 es diferente de 3")

if 5 >= 3:
    print("5 es mayor o igual a 3")

if 5 <= 5:
    print("5 es menor o igual a 3")

if 5 > 3:
    print("5 es mayor que 3")

if 5 < 3:
    print("5 es menor que 3")
