'''Escreva uma função que receba dois números e retorne True se o 
primeiro número for múltiplo do segundo. Valores esperados:

● Múltiplo(8,4) == True
● Múltiplo(7,3) == False
● Múltiplo(5,5) == True
'''

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero:"))

def multiplo(a,b):
    if (a%b) == 0:
        return True
    else:
        return False

#resultado = multiplo(num1,num2)
#print(resultado)
print(multiplo(num1,num2))