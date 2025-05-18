bestseller = str(input(“o livro é um best-seller? S / N : “)).upper()
ano = str(input(“o livro foi lançado a mais de 5 anos? S / N : “)).upper()
quantidade = int(input(“Quantos livros o cliente comprou?”))
preco = float(input(“Qual o valor do livro? “))
desconto = 0

if bestseller == “S” or ano == “S”:
  desconto += 5
  if quantidade > 3:
    desconto += 5

precofinal = preco * (1 – desconto / 100) * quantidade

print(f ‘ O preço final será de R${precofinal:.2f})
