# Haga un codigo que usando for y while tome una lista de numeros y los devuelva ordenados de menor a mayor

lista = [2,5,3,6,1,9,2,10,7,12]

# Ordenar la lista
while True:
    cambio = False
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            cambio = True
    if not cambio:
        break

print(lista)