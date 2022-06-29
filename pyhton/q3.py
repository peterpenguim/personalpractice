salarios = []
filhos = []
salarios_menores = []
while True:
    entrada = input()
    if entrada == "-1":
        break
    else:
        entrada = entrada.split()
        entrada_int = [int(x) for x in entrada]
        salarios.append(entrada_int[0])
        filhos.append(entrada_int[1])

media_salario = sum(salarios) / len(salarios)

media_filhos = sum(filhos) / len(filhos)

maior_salario = max(salarios)

for i in salarios:
    if i <= 2500:
        salarios_menores.append(i)
percentual = len(salarios_menores) / len(salarios)

print(f'{media_salario} {media_filhos} {maior_salario} {percentual}')