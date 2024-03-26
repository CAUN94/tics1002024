# Extras y muy importantes, en un if o elif se puede hacer varias comparaciones

# Los comandos para esto son "and" y "or" y funcionan igual que la logica

x = 10
y = 8

if x > 5 and y > 7:
    print(f"{x} es mayor a 5 y {y} es mayor a 7")
elif x > 5 and y < 7:
    print(f"{x} es mayor a 5 y {y} es menor a 7")
elif x < 5 and y < 7:
    print(f"{x} es menor a 5 y {y} es menor a 7")

if x > 5 or y > 7:
    print(f"{x} es mayor a 5 o {y} es mayor a 7")
elif x > 5 or y < 7:
    print(f"{x} es mayor a 5 o {y} es menor a 7")
elif x < 5 or y < 7:
    print(f"{x} es menor a 5 o {y} es menor a 7")

# Tambien podemos poner un if dentro de otro if (y dentro de otro y dentro de otro)
    
# Por ejemplo veamos si alguien es mayor de edad para entrar a la disco, en caso de que si vemos si es hombre o mujer ya que la entrada de hombre cuesta 20 y la de mujer 18 y finalmente ver si es alumno de la univerdad porque tiene un descuento del 20% si lo es.
    
