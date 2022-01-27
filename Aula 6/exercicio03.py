'''
Faça uma calculadora com as quatro operações básicas
matemáticas. Informe ao usuário caso ele realize uma divisão
por zero.
'''

N1 = float(input("Digite o primeiro numero para o calculo: "))
caractere = input("Digite (+) para soma, (-) para subtração, (*) para multiplicação e (/) divisão: ")
N2 = float(input("Digite o segundo numero para o calculo: "))

if caractere == '+':
    result = N1 + N2
    print(f"A soma dos valores é:  {result}")
elif caractere == '-':
    result = N1 - N2
    print(f"A subtração dos valores é: {result}")
elif caractere == '*':
    result = N1 * N2
    print(f"A multiplicação dos valores é:{result}")
elif caractere == '/':
    if N2 == 0:
        print("Não é possivel dividir por zero!!!")
    else:
        result= N1/N2
        print(f"A divisao dos valores é:{result}")
else:
    print("Operação inválida!!!")      
    
