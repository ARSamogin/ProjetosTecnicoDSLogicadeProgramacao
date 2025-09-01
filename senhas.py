import random
import string

def gerador():
    while True:
        print("-~-~-~-GERADOR DE SENHAS-~-~-~-")
        print("Gere senhas de 6 a 19 caracteres")
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ""
        tam = int(input("Digite o tamanho da senha: "))
        if tam <= 5 or tam >=20:
            print("Digite uma quantidade de 6 a 19 caracteres")
        else:
            for i in range(tam):
                senha += random.choice(caracteres)
        print(f'Senha Gerada: {senha}')

gerador()
