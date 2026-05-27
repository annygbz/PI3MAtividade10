consumo_total = 0

for i in range(1, 8):
    consumo = float(input(f"Digite o consumo do produto {i}: "))

    consumo_total += consumo

    if i == 1:
        maior_consumo = consumo
        produto_maior = i
    else:
        if consumo > maior_consumo:
            maior_consumo = consumo
            produto_maior = i

print("O consumo total é de:", consumo_total, "kg")
print("O produto que mais consome matéria-prima é o de número:", produto_maior)