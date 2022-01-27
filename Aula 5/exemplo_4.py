'''
Calcular a conta de um telefone celular. Os planos da empresa 
apresentam planos diferenciados de acordo com a 
quantidade de minutos usados por mês. Abaixo de 200 minutos, 
a empresa cobra R$ 0,20 por minuto. Entre 200 a 400 minutos, 
o preço é de R$ 0,18. Acima de 400
minutos, o preço por minuto é de R$ 0,15.
'''

minutos = int(input("Quantos minutos voce voce utilizou?"))

if minutos < 200:
    preco = minutos * 0.20
else:
    if minutos <= 400:

        preco = minutos * 0.18
    else:

        preco = minutos * 0.15
print(f"O valor a pagar é de: {preco}")