



'''
def inteiros(n):
    return len((str(n)))

n = str(input('Digite um número: ')).strip()
print(f'Esse número tem {inteiros(n)} dígitos')'''


def qtde(n):
    s = str(n)
    return len(s)

def menu():
    numero = int(input("Digite um numero qualquer: "))
    resultado = qtde(numero)
    print(f"A quantidade de caracteres é: {resultado}")

menu()