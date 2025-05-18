av1 = float(input("Digite a nota que você recebeu na avaliação 1: "))
av2 = float(input("Digite a nota que você recebeu na avaliação 2: "))
provafinal = float(input("Digite a nota que você recebeu na prova final: "))
provapaulista = float(input("Digite a nota que você recebeu na paulista: "))

pesoav1 = av1 * 0.2
pesoav2 = av2 * 0.2
pesopf = provafinal * 0.3
pesopp = provapaulista * 0.3

media = pesoav1 + pesoav2 + pesopf + pesopp

if media >= 5 and media <=10:
    print("Parabéns, você alcançou a média bimestral")
    print(media)
elif media >=0 and media <5:
    print("Você não consegiu alcançar a média bimestral, estude mais")
    print(media)
else:
    print("Você inseriu alguma nota errada")
    print(media)
