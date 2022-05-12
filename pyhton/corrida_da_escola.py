#THE HUXLEY 207
entradas = input().split()
somas = []
entradas_int = [int(x) for x in entradas]
    
for i in range(entradas_int[0]):
    tempos = input().split()
    tempos_int = [int(x) for x in tempos]
    soma = sum(tempos_int)
    somas.append(soma)
print(somas.index(min(somas))+ 1) 


