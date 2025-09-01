import random
import string

def gerador():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    tamanho = int(input("Digite o tamanho da senha: "))
    senha = ""
    for i in range(tamanho):
        senha += random.choice(caracteres)
    print(senha)

gerador()