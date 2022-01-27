'''
Escreva um programa que pergunte a velocidade do 
carro de um usuário. Caso ultrapasse 80 km/h,
exiba uma mensagem dizendo que o usuário foi 
multado. Neste caso, exiba o valor da multa, 
cobrando R$ 5,00 por km acima de 80 km/h.
'''

vel = float(input("Digite a velocidade do carro: "))
if vel > 80:
    multa = 5*(vel-80)
    print(f"A multa para a velocidade de {vel} km/h é de R$ {multa}")