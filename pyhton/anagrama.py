tamanho = int(input())

palavra1 = list(input())
palavra2 = list(input())

for i in range(len(palavra1)):
    if "," in palavra1:
        palavra1.remove(",")
    if "." in palavra1:
        palavra1.remove(".")
    if " " in palavra1:
        palavra1.remove(" ")

for i in range(len(palavra2)):
    if "," in palavra2:
        palavra2.remove(",")
    if "." in palavra2:
        palavra2.remove(".")
    if " " in palavra2:
        palavra2.remove(" ")
    
palavra1.sort()
palavra2.sort()

if palavra1 == palavra2:
    print("S")
else:
    print("N")