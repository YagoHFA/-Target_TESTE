frase = str(input("Insira uma frase"))
reverseFrase = ''

for n in frase[::-1]:
    reverseFrase += n

print(reverseFrase)