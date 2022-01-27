'''
Programa que solicita o valor da faixa salarial do usuário e 
informa qual é a porcentagem de imposto de renda na qual o
mesmo deve pagar. Levando em consideração: Salários menores 
que R$ 1000,00 não pagam impostos; Salários entre R$ 1000,00 e 
R$ 3000,00 paga 20%; Salários acima de R$
3000,00 paga 35% de imposto.
Pressione Shift + Tab para acessar o histórico do bate-papo.
'''

salario = float(input("Informe seu salario para saber a porcentagem encima dele: "))
if salario<1000:
    print("Não paga imposto")
if salario>=1000 and salario <= 3000:
    print("paga 20%","de imposto")
if salario>3000:
    print("paga 35%","de imposto")


