'''
Crie um programa que resolva o seguinte problema:
Um triângulo será equilátero se seus três ângulos são iguais.
Um triângulo com dois de seus ângulos iguais é chamado de isósceles.
Um triângulo com três ângulos diferentes é chamado de escaleno.
A soma dos três ângulos de um triângulo deverá ser 180º, senão não é um triângulo.
'''

A = float(input("Digite o 1° Ângulo do triângulo: "))
B = float(input("Digite o 1° Ângulo do triângulo: "))
C = float(input("Digite o 1° Ângulo do triângulo: "))

if A + B + C == 180.0:
    print("É um triângulo, vamos ver qual tipo de triângulo ele é: ........")
    if A == B or B == C:
        print("Triângulo equilatero!!!")
    elif A == B or B == C or A == C:
        print("É um triangulo isóseles!!!")
    else:
        print("É um triângulo escaleno!!!")
else:
    print("Desculpe, mas essa figura não é um triângulo.")