import math
a = input().split()
intA = [int(x) for x in a]
b = input(). split()
intB = [int(x) for x in b]
c = input().split()
intC = [int(x) for x in c]

distanciaAC = math.sqrt(pow((intC[0] - intA[0]),2) + pow((intC[1] - intA[1]),2))
distanciaBC = math.sqrt(pow((intC[0] - intB[0]),2) + pow((intC[1] - intB[1]),2))

if distanciaAC < distanciaBC:
  print(f"A - {distanciaAC:.2f}")
else:
  print(f"B - {distanciaBC:.2f}")