valores = []
v = 1
while v != 0:
    teste = int(input())
    valores.append(teste)
    v = teste

valores.remove(0)

def qtd_notas(teste):
    valor1 = teste // 50
    resto50 = teste % 50

    valor2 = resto50 // 10
    resto10 = resto50 % 10

    valor3 = resto10 // 5
    resto5 = resto10 % 5

    valor4 = resto5 // 1

    print("{} {} {} {}\n".format(valor1, valor2, valor3, valor4))

n = 1
for valor in valores:
    print("Teste {}".format(n))
    qtd_notas(valor)
    n += 1