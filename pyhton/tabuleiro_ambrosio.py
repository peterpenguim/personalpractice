#THE HUXLEY 2410
ultima_casa = int(input())
contador = []
casa = 1
n = 1
while casa != ultima_casa:
    if casa > ultima_casa:
        casa = casa - ultima_casa
        contador.append(casa)
    else:
        contador.append(casa)
    casa += n
    n += 1
    if n >= 6:
        n = 1
print(len(contador))
