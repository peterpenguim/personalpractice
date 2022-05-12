copas = ['01C','02C','03C','04C','05C','06C','07C','08C','09C','10C','11C','12C','13C']
espadas = ['01E','02E','03E','04E','05E','06E','07E','08E','09E','10E','11E','12E','13E']
ouros = ['01U','02U','03U','04U','05U','06U','07U','08U','09U','10U','11U','12U','13U']
paus = ['01P','02P','03P','04P','05P','06P','07P','08P','09P','10P','11P','12P','13P']
copas_copy = copas.copy()
espadas_copy = espadas.copy()
ouros_copy = ouros.copy()
paus_copy = paus.copy()
baralho = []

cartas = input()
n = 3
m = 0
for i in range(len(cartas) // 3):
  baralho.append(cartas[m:n])
  n = n + 3
  m = m + 3
for carta in baralho:
  if carta in copas:
    copas.remove(carta)
  if carta in ouros:
    ouros.remove(carta)
  if carta in espadas:
    espadas.remove(carta)
  if carta in paus:
    paus.remove(carta)

c = len(copas)
e = len(espadas)
u = len(ouros)
p = len(paus)

for carta in baralho:
    if baralho.count(carta) > 1:
        if carta in copas_copy:
            c = "erro"
        if carta in espadas_copy:
            e = "erro"
        if carta in ouros_copy:
            u = "erro"
        if carta in paus_copy:
            p = "erro"

print(f"{c}\n{e}\n{u}\n{p}")