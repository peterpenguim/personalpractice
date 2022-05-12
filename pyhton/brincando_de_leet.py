#THE HUXLEY 1165
string = list(input())
lista_invertida = []
substituicoes = []

n = -1
for i in range(len(string)):
    lista_invertida.append(string[n])
    n -= 1

for letra in lista_invertida:
    if letra == "A" or letra == "a":
        posicao = lista_invertida.index(letra)
        lista_invertida.remove(letra)
        lista_invertida.insert(posicao, "@")
        substituicoes.append(1)

    if letra == "E" or letra == "e":
        posicao = lista_invertida.index(letra)
        lista_invertida.remove(letra)
        lista_invertida.insert(posicao, "3")
        substituicoes.append(1)

    if letra == "I" or letra == "i":
        posicao = lista_invertida.index(letra)
        lista_invertida.remove(letra)
        lista_invertida.insert(posicao, "1")
        substituicoes.append(1)

    if letra == "O" or letra == "o":
        posicao = lista_invertida.index(letra)
        lista_invertida.remove(letra)
        lista_invertida.insert(posicao, "0")
        substituicoes.append(1)

    if letra == "T" or letra == "t":
        posicao = lista_invertida.index(letra)
        lista_invertida.remove(letra)
        lista_invertida.insert(posicao, "7")
        substituicoes.append(1)

    if letra == "S" or letra == "s":
        posicao = lista_invertida.index(letra)
        lista_invertida.remove(letra)
        lista_invertida.insert(posicao, "5")
        substituicoes.append(1)

if len(string) == 0:
        print("vazio")
        print(0)
else:
    for caractere in string:
        if caractere.isnumeric() == True:
            print("numeros")
            print(0)
            break
    else:
        str = "".join(lista_invertida)
        print(str)
        print(len(substituicoes))