ultima_casa = int(input())
contador = []
casa = 1
while True:
    if casa == ultima_casa:
        break
    else:
        contador.append(casa)
        casa = casa + 2
        if casa == ultima_casa:
            break
        else:
            contador.append(casa)
            casa = casa + 3
            if casa == ultima_casa:
                break
            else:
                contador.append(casa)
                casa = casa + 4
                if casa == ultima_casa:
                    break
                else:
                    contador.append(casa)
                    casa = casa + 5
                    if casa == ultima_casa:
                        break
                    else:
                        contador.append(casa)
                        casa = casa + 6
                        if casa == ultima_casa:
                            break
                        else:
                            contador.append(casa)
print(len(contador) + 1)