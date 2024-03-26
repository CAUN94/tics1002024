# Finalmente tenemos el elif que es una combinación de if y else, ya que evalua una condición y si esta no se cumple evalua otra condición
# La diferencia que tiene con el else es que el elif puede tener una condición y solo puede haber un else por if, mientras que puedo poner todos los elif que quiera.

# Ejemplo 1:

# x = 18
# if x > 19:
#     print("x es mayor a 19")
# elif x == 19:
#     print("x es igual a 19")
# else:
#     print("x es menor a 19")

# Ejemplo 2: (Muchos elif)

x = int(input('Numero:'))

if x > 19:
    print("Mayor a 19")
elif x > 18:
    print("Mayor a 18")
elif x > 17:
    print("Mayor a 17")
elif x > 16:
    print("Mayor a 16")
elif x > 15:
    print("Mayor a 15")


# Ejemplo 3: 


# Notemos que no hay un else
    
