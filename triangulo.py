from math import sqrt

a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))
perimetro = a + b + c
sp = perimetro / 2
area = sqrt(sp * (sp - a) * (sp - b) * (sp - c))

if a == b == c:
    print(f'O Triângulo é Equilátero, seu perímetro é de {perimetro} e sua área é de {area:.2f}')
elif a == b or b == c or a == c:
    print(f'O Triângulo é Isóceles, seu perímetro é de {perimetro} e sua área é de {area:.2f}')
else:
    print(f'O Triângulo é Escaleno, seu perímetro é de {perimetro} e sua área é de {area:.2f}')
