soma = 0

for i in range(5):
    numero = float(input("Digite um número: "))

    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    soma += numero

media = soma / 5

print("O maior número é:", maior)
print("O menor número é:", menor)
print("A média desses números é:", media)