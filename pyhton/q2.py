funcionarios = []
tempos = []
while True:
    matricula = input()
    if matricula == "0 0 0 0 0":
        break
    else:
        matricula = matricula.split()
        matriculas = [int(x) for x in matricula]
        funcionarios.append((matriculas))

for i in funcionarios:
    tempo = ((i[4] * 12) - (i[2] * 12)) + (i[3] - i[1])
    tempos.append(tempo)

posicao = tempos.index(max(tempos))

print(funcionarios[posicao][0])