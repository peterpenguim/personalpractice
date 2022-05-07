import  random

lista = list(range(101))
elem = lista[random.randint(0,101)]
inicio = 0
fim = len(lista) -1
meio = (fim + inicio) // 2
tentativas = []

print('Elemento = {}'.format(elem))

while inicio <= fim:
    meio = (fim + inicio) // 2
    chute = lista[meio]
    print(chute)
    tentativas.append(chute)
    if elem == chute:
        print('Acertou!')
        break
    elif chute > elem:
        fim = meio - 1
    else:
        inicio = meio + 1
        
print('Tentativas = {}'.format(len(tentativas)))