estado = {
   "SP"  : 67836.43,
    "RJ" : 36678.66,
    "MG" : 29229.88,
    "ES" : 27165.48,
    "Outros" : 19849.53
}

Porcento = sum(estado.values())
print(Porcento)
print(len(estado))
aux = 0


for x in estado:
  aux = estado[x] * 100
  aux = aux / Porcento
  print(f'Estado: {x}, Porcentagem:  {"%.2f" % aux}%')