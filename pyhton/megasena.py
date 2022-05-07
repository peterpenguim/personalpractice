import random
A = list(range(10))
B = list(range(10))

random.shuffle(A)
random.shuffle(B)

sorteio = []

while len(sorteio) < 6:
  valA = A[random.randint(0,9)]
  valB = B[random.randint(0,9)]
  valor_sorteado = '{}{}'.format(valA,valB)
  if valor_sorteado != '00' and valor_sorteado not in sorteio:
    sorteio.append(valor_sorteado)
print(sorteio)