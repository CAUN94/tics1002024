# Finalmente tenemos el elif que es una combinación de if y else, ya que evalua una condición y si esta no se cumple evalua otra condición
# La diferencia que tiene con el else es que el elif puede tener una condición y solo puede haber un else por if, mientras que puedo poner todos los elif que quiera.

# Ejemplo 1:

x = 5

if x > 4:
    print(f"{x} es mayor que 4")

elif x == 4:
    print(f"{x} es igual a 4")

else:
    print(f"{x} es menor que 4")

# Ejemplo 2: (Muchos elif)
    
x = 20

if x > 20:
    print(f"{x} es mayor que 20")
elif x > 15:
    print(f"{x} es mayor que 15")
elif x > 10:
    print(f"{x} es mayor que 10")
elif x > 5:
    print(f"{x} es mayor que 5")
else:
    print(f"{x} es menor que 5")

# Ejemplo 3: 
    
x = 10
if x > 5:
    print(f"{x} es mayor que 5")
elif x % 2 == 0:
    print(f"{x} es par")

# Notemos que no hay un else
    
