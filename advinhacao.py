from random import randint

def advinhacao():
    secreto = randint(0, 100)
    tentativas = 0

    while True:
        chute = int(input("Tente adivinhar o número de 0 a 100: "))
        tentativas += 1

        if secreto > chute:
            print("Chutou baixo")
        elif secreto < chute:
            print("Chutou alto ")
        else:
            print(f"Você acertou!!! O número era {secreto} e levou {tentativas} tentativas para acertar.")
            break

while True:
    advinhacao()
    continuar = str(input("Quer jogar de novo? s / n?")).lower().strip()
    if continuar != "s":
        break
