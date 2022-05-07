inscritos = int(input())
lista_cpf = []
lista_notas = []

for i in range(inscritos):
    cpf = int(input())
    lista_cpf.append(cpf)

for i in range(inscritos):
    notas = int(input())
    lista_notas.append(notas)

testes = int(input())

for i in range(testes):
    escolhidos = int(input())
    if escolhidos in lista_cpf:
        posicao = lista_cpf.index(escolhidos)
        print(lista_notas[posicao])
    else:
        print('NAO SE APRESENTOU')