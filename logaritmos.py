from math import log10

def main():
    while True:
        print("Calculadora de Escalas Logaritmas")
        print("Escolha uma opção: \n" \
        "1 - pH \n"
        "2 - Richter \n" \
        "3 - Sair")
        opcao = int(input("Escolha sua opção: "))

        if opcao == 1:
            ph()
        elif opcao == 2:
            richter()
        elif opcao == 3:
            print("Saindo")
            break
        else:
            print("Digite uma opção válida")

def ph():
    print("Calculadora de pH")
    print("-----------------")

    while True:
        print("Digite 0 para sair do programa")
        h3o = float(input("Digite a quantidade de h3o/mol na formula: "))
        
        if h3o == 0:
            print("Saindo")
            break

        else:
            pH = -1 * log10(h3o)

            if pH > 7 and pH <= 14:
                print(f'O pH da substância é de {pH:.2f}, que é considerado Alcalino')
            elif pH > 0 and pH < 7:
                print(f'o pH da substância é de {pH:.2f}, que é considerado Ácido')
            elif pH == 7:
                print(f'O pH da substância é de {pH:.2f}, que é considerado neutro')
            else:
                print("O pH não pode ser calculado, ou porque algum dado é inválido ou a substância é muito ácida ou alcalina para essa escala")


def richter():
    print("Escala Richter")
    print("--------------")

    while True:
       print("Escolha uma opção: \n" \
       "1 - Joules para Richter \n" \
       "2 - Richter para Joules \n" \
       "3 - Sair do programa")
       opcao = int(input("Opção: "))

       if opcao == 1:
          energia = float(input("Digite a quantidade de energia(Joules): "))
          if energia <= 0:
              print("Quantidade de energia inválida!")
          else:
              magnetude = (log10(joules) - 4.8) / 1.5
              print(f'O terremoto é de {magnetude:.2f} da escala Richter')
       elif opcao == 2:
           magnetude = float(input("Digite a magnetude do terremoto: "))
           if magnetude <= 0:
               print("Mangetude inválida")
           else:
               joules = 10 ** (1.5 * magnetude + 4.8)
               print(f'O Equivalente em Joules é de {joules:.2f}')
       elif opcao == 3:
           print("Saindo")
           break  
       
if __name__ == '__main__':
    main()
