'''Escreva uma função que receba o lado de um quadrado e retorne 
sua área (A=lado²). Valores
esperados:
● Área_quadrada(4) == 16
● Área_quadrada(9) == 81e
'''

num1: int(input('Digite o lado do quadrado: '))


def quadrado(a):
    resultado = a**2
    return resultado

print(f"A area do quadro é: {quadrado(num1)}")