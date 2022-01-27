'''
Escreve um programa que pergunte o salário do funcionário 
e  calcule o valor do aumento. Para salários
superiores a R$ 1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, de 15%.
'''

salario = float(input("Qual o seu Salario para calculo de aumento:"))

if salario > 1250:
    aumento = salario * .10
else: 
    salario < 1250
    aumento = salario * .15
print("Seu salario teve um aumento %6.2f" % aumento)