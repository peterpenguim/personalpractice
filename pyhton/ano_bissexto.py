#THE HUXLEY 3725
anos = []
while True:
    year = int(input())
    if year == -1:
        break
    else:
        anos.append(year)

for ano in anos:
    if len(str(ano)) < 4:
        print("Ano invalido")
    else:
        resto1 = ano % 4
        resto2 = ano % 400
        resto3 = ano % 100
        if resto1 == 0:
            if resto2 == 0 or resto3 != 0:
                if ano == 2152:
                    print(f"O ano {ano} eh bissexto")
                elif ano > 2152:
                    print(f"O ano {ano} serah bissexto")
                else:
                    print(f"O ano {ano} foi bissexto")
            else:
                print(f"O ano {ano} NAO eh bissexto")
        else:
            print(f"O ano {ano} NAO eh bissexto")