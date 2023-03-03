import json

with open("dados.json", encoding='utf-8') as diario_json:
    dados = json.load(diario_json)

valorMax = 0
valorMin = 100000000000
diaUteis = len(dados)
soma = 0
countMedia = 0

for n in range(len(dados)):
    if(dados[n]['valor'] > valorMax):
        valorMax = dados[n]['valor']
       
    if(dados[n]['valor'] < valorMin and dados[n]['valor'] != 0):
        valorMin = dados[n]['valor']
        
    if(dados[n]['valor'] == 0):
        diaUteis -= 1
    soma += dados[n]['valor']
for n in range(len(dados)):
    if(dados[n]['valor'] > (soma / diaUteis)):
        countMedia += 1
print(valorMin)
print(valorMax)
print(countMedia)
