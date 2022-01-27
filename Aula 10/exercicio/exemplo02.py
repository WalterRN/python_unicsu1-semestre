'''Escreva uma função que imprima o maior de dois números. Valores esperados:'''
''' 
●   Máximo(5,6) == 6
●   Máximo(2,1) == 2
●   Máximo(7,7) == 7
'''

num1:  int(input("Digite o primeiro numero:"))
num2:  int(input("Digite o segundo numero:"))


def maior(a,b):
    if a > b:
        print(f'o número {a} é maior')
    else:
        print(f'O número {b} é maior')

maior(num1, num2)    