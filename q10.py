total = 0
vendas = []

for i in range(1, 7):
    valor = float(input(f"Digite o valor de vendas do mês {i}: "))
    vendas.append(valor)
    total += valor

media = total / 6

acima_media = 0

for venda in vendas:
    if venda > media:
        acima_media += 1

print("Total de vendas no período:", total)
print("A média mensal é de:", media)
print("A quantidade de meses acima da média foi:", acima_media)