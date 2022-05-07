cidades = []
distancias = []
valores = []
while True:
    cidade = input().lower()
    if cidade == "FIM".lower():
        break
    else:
        if cidade != "":
            cidades.append(cidade)
        distancia = int(input())
        distancias.append(distancia)
        valor = float(input())
        valores.append(valor * 2)

if len(cidades) == 0:
    print("SEM DESTINO")
else:
    for i in distancias:
        posicao = distancias.index(max(distancias))

    if valores[posicao] <= 300:
        for i in cidades:
            print(cidades[posicao].upper())
            break
    else:
        cidades.remove(cidades[posicao])
        distancias.remove(distancias[posicao])
        valores.remove(valores[posicao])
        posicao = distancias.index(max(distancias))
        if valores[posicao] <= 300:
            for i in cidades:
                print(cidades[posicao].upper())
                break