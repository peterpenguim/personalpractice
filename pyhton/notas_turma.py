#THE HUXLEY 1285
import statistics
contador = []
respostas = []
notas = []
turma = {}
while True:
    alunos = input()
    if alunos == "*":
        break
    else:
        alunos = alunos.split()
        turma[alunos[0]] = alunos[1]

for valores in turma.values():
    respostas.append(valores)

gabarito = input()

for resposta in respostas:
    n = 0
    for i in range(5):
        if resposta[n] == gabarito[n]:
            contador.append(resposta[n])
            n += 1
        else:
            n += 1
    notas.append(len(contador))
    contador.clear()

print(f"Maior: {max(notas)}")
print(f"Menor: {min(notas)}")
print(f"Media: {statistics.mean(notas):,.2f}")