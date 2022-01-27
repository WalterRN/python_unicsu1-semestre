'''
programa que solicita a idade do carro do usuário e, 
em seguida, escreva "novo" se o carro
tiver menos de trÊ anos; ou "velho", caso contrario.
'''

idade = int(input("digite a idade do seu carro: "))
if idade<= 3:
    print("seu carro é novo!!!")
if idade > 3:
    print("seu carro é velho!!!")