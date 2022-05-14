valores = []
candidatos = {}
while True:
    candidato = input()
    if candidato == "FIM".lower():
        break
    else:
        candidato = candidato.split()
        for i in range(int(candidato[-1])):
            anuncio = input()
            if anuncio == "internet":
                valores.append(3000)
            elif anuncio == "revista":
                valores.append(750)
            elif anuncio == "outdoor":
                valores.append(1500)
            elif anuncio == "radio":
                radio = input()
                if radio == "fm":
                    valores.append(500)
                elif radio == "am":
                    valores.append(300)
            elif anuncio == "tv":
                hora = int(input())
                if hora <= 20:
                    valores.append(1200)
                elif hora > 20:
                    valores.append(2000)
        candidatos[candidato[0]] = sum(valores)
for chave, valor in candidatos.items():
    print(f"{chave}: {valor}")
