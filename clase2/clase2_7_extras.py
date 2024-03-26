# Extras y muy importantes, en un if o elif se puede hacer varias comparaciones

# Los comandos para esto son "and" y "or" y funcionan igual que la logica
if True and True:
    print(True)
if True and False:
    print(True)
x = 25
if 20 <= x <= 30:
    print("Cumples con la edad")

# Tambien podemos poner un if dentro de otro if (y dentro de otro y dentro de otro)
    
# Por ejemplo veamos si alguien es mayor de edad para entrar a la disco, en caso de que si vemos si es hombre o mujer ya que la entrada de hombre cuesta 20 y la de mujer 18 y finalmente ver si es alumno de la univerdad porque tiene un descuento del 20% si lo es.
    
edad = int(input("Edad: "))

if edad >= 18:
    print("Puedes entrar")
    genero = input("Eres hombre o mujer")
    estudiante = input("Eres estudiante? Si/No")
    if genero == 'mujer':
        if estudiante == 'Si':
            print("Debes pagar",18*0.8)
        else:
            print("Debes pagar",18)
    elif genero == 'hombre':
        if estudiante == 'Si':
            print("Debes pagar",20*0.8)
        else:
            print("Debes pagar",20)
else:
    print("No puedes entrar")