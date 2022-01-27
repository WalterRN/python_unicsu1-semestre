

def tipo(x):
    if x < 0:
       return "N"
    elif x>0:
        return "P"
    else:
        return 0

def menu():
    num = int(input("Digite um numero quaquer: "))
    resultado = tipo(num)
    print(f"O resultado é: {resultado}")

menu()
        
