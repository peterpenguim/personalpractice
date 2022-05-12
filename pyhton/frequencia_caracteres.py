#THE HUXLEY 2835
str = input()
str = sorted(str, reverse = True)

dicionario = {}
for letra in str:
    dicionario[letra] = str.count(letra)
for chave, qtd in dicionario.items():
    print("{} {}".format(chave, qtd))