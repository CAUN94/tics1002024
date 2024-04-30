import random 

dados = []
for i in range(5):
    dados.append(random.randint(1, 6))
dados = [1, 1, 2, 3, 3]
dados.sort()

print('Sus dados son:', dados)

while True:
    # caso 1: escala real
    escalara_real = 1
    for i in range(1, len(dados)):
        if dados[i-1] != dados[i] - 1:
            escalara_real = 0
    if escalara_real == 1:
        print('Escalera real')
        break
    # caso 2: escalera pequeña
    if dados.count(1) <= 1 and dados.count(2) <= 1 and dados.count(3) <= 1 and dados.count(4) <= 1 and dados.count(5) <= 1:
        print('Escalera pequeña')
        break
    
    # caso 3: full house, un par y un trio
    full_house = 0
    if (dados.count(dados[0]) == 2 and dados.count(dados[4]) == 3 or (dados.count(dados[0]) == 3 and dados.count(dados[4]) == 2)):
        print('Full house')
        full_house = 1
        break
    
    # caso 4: escalera pequeña, cuatro dados consecutivos
    escalara_pequeña = 1
    for i in range(1,3):
        if dados[i-1] != dados[i] - 1:
            escalara_pequeña = 0
    if escalara_pequeña == 1:
        print('Escalera pequeña')
        break

    
    # caso 5: triple
    if dados.count(1) == 3 or dados.count(2) == 3 or dados.count(3) == 3 or dados.count(4) == 3 or dados.count(5) == 3 or dados.count(6) == 3:
        print('Triple')
        break

        # caso 5: triple
    if dados.count(1) == 2 or dados.count(2) == 2 or dados.count(3) == 2 or dados.count(4) == 2 or dados.count(5) == 2 or dados.count(6) == 2:
        print('Par')
        break