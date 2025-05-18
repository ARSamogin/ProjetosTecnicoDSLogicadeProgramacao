texto = str(input(“Insira o texto para ser analisado: ”)).lower()
letra = str(input(“Digite o caractere para ser contado: “)).lower()
contagem = 0

for i in texto:
​  if i == letra:
​    contagem += 1
    print(f’ A quantidade de caracteres {letra} é de {contagem}’)
