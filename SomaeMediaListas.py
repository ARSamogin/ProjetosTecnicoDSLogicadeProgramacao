numeros = [8, 4, 2, 5, 6, 1, 5, 7, 3, 7, 8, 3, 1]
soma = 0

for num in numeros:
    soma += num

media = soma / len(numeros)

print(f'A soma é {soma} e a média é {media:.2f}')