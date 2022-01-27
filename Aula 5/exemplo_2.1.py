'''
Escreva um programa que leia três
Números e que imprima o
maior e o menos.
'''


primeiro = int(input('Primeiro numero: '))
segundo = int(input('Segundo numero: '))
terceiro = int(input('Terceiro numero: '))



maior = primeiro
if(segundo > maior):
    maior = segundo
if(terceiro > maior):
    maior = terceiro


menor = primeiro
if(segundo < menor):
    menor = segundo
if(terceiro < menor):
    menor = terceiro

print(f"O maior é: {maior} e o menor é {menor}")


