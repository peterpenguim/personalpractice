quantidade = int(input())
elementos = input().split()
correcoes = []
posicao1 = 0
posicao2 = -1

for i in range(len(elementos)//2):
    if elementos[posicao1] != elementos[posicao2]:
        correcoes.append(1)
        posicao1 += 1
        posicao2 -= 1
    else:
        posicao1 += 1
        posicao2 -= 1
print(len(correcoes))