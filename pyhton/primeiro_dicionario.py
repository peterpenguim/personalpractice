dicionario = {}
especiais = '."(*$#:'
words = []
while True:
    palavras = input().lower()
    if palavras == "-1":
        break
    else:
        for palavra in palavras:
            if palavra in especiais:
                palavras = palavras.replace(palavra, " ")
        palavras = palavras.split()
        words.extend(palavras.copy())
words.sort()

for word in words:
    dicionario[word] = words.count(word)

for chave, valor in dicionario.items():
    print(f"{chave} {valor}")