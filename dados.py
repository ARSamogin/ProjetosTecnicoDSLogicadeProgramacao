from random import randint

def main():
    while True:
        resultados = []
        validos = [4, 6, 8, 10, 12, 20, 100]
        print("--Simulador de Dados--")
        dado = int(input("Selecione qual dado de RPG você deseja: "))
        if dado not in validos:
            print("Dado Inválido!")
            pass
        else:
            quantidade = int(input("Quantos dados você quer rolar? "))
            if quantidade <= 0:
                print("Quantidade inválida!")
            else:
                for i in range(quantidade):
                    rolagem = randint(1, dado)
                    resultados.append(rolagem)
            
            print(f'A soma das rolagens foram: {sum(resultados)}')
            print(f'As rolagens foram: {resultados}')

main()
