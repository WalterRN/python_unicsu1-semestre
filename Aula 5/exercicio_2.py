'''
Escreva um programa que leia três
Números e que imprima o
maior e o menos.
'''

primeiro = int(input("Número um: "))
segundo = int(input("Número dois: "))
terceiro = int(input("Número três: "))

if primeiro > segundo and primeiro > terceiro:
    print("O número um é o maior: ", primeiro)
elif segundo > primeiro and segundo > terceiro:
    print("O número dois é o maior: ", segundo)
elif terceiro > primeiro and terceiro > segundo:
    print("O número três é o maior: ", terceiro)


