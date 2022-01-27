'''
Crie um programa que resolva o seguinte problema:
Um triângulo será equilátero se seus três ângulos são iguais.
Um triângulo com dois de seus ângulos iguais é chamado de isósceles.
Um triângulo com três ângulos diferentes é chamado de escaleno.
A soma dos três ângulos de um triângulo deverá ser 180º, senão não é um triângulo.
'''

r1 = int(input("Digite o primeiro lado do triangulo: "))
r2 = int(input("Digite o segundo lado do triangulo: "))
r3 = int(input("Digite o primeiro lado do triangulo: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print("equilatero")
    elif r1 != r2 != r3:
        print("esqualeno")
    else:
        print("esosceles")
else:
    print("os seguimentos acima  nao podem formar triangulo")