'''
Faça uma calculadora com as quatro operações básicas
matemáticas. Informe ao usuário caso ele realize uma divisão
por zero.
'''



a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
op = input("Digite a operação: ")



if op=="+":
  print("A soma dos valores é: ", (a+b))
elif op=="-":
  print("A subtração dos valores é: ",(a-b))
elif op=="*":
  print("A multiplicação dos valores é: ",(a*b))
elif op=="/":
  if b == 0:
    print("Não é possível dividor por zero.")
  else:
    print("A divisao dos valores é: ", (a/b))
else:
  print("Operação inválida!!!")