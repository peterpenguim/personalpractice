torres = int(input())
tamanhos = input().split()

tamanhos_int = [int(x) for x in tamanhos]
ocorrencias = []

for i in tamanhos_int:
    ocorrencias.append(tamanhos_int.count(i))
print(max(ocorrencias), len(set(tamanhos_int)))

