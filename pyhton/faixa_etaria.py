#THE HUXLEY 3861
idades = []
while True:
    age = int(input())
    if age == 0:
        break
    else:
        idades.append(age)

for idade in idades:
    if idade < 0:
        print("Você ainda não nasceu.")
    elif idade <= 11:
        print("Você é uma criança.")
    elif idade <= 17:
        print("Você é um adolescente.")
    elif idade <= 35:
        print("Você é um jovem.")
    elif idade <= 64:
        print("Você é um adulto.")
    elif idade >= 65:
        print("Você é um idoso.")