fibonati = int(input("Digite o número a ser verificado: "))

count = 1
aux = 0

while count < fibonati:
    soma = count
    count += aux
    print(count)
    aux = soma
if(count == fibonati):
    print("Faz parte da sequencia de fibonati")
else:
    print("Não faz parte da sequencia de fibonati")