'''
Programa que adiciona elemento à lista de forma continua e 
imprime os elementos após
encerrado. Ao digitar 0 (zero) o programa é encerrado.
'''


L=[]

while True:
    n=int(input("Digite um numero (0 para sair)"))
    if n==0:
        break
    L.append(n)

x=0
while x < len(L):
    print(L[x])
    x+=1