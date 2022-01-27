peso = float(input("Digite o peso:"))
altura = float(input("Digite o altura:"))

def IMC(a,b):
    return a / (b * b)
    
def situacao(imc):
    if imc >= 18.50 and imc <= 24.99:
        print("peso normal")
    elif imc >= 25 and imc <= 29.99:
        print("Acima do peso")
    elif imc >= 30 and imc <= 39.99 :
        print("Obesidade I")
    elif imc >= 35 and imc <= 39.99:
        print("Obesidade II")
    
imc = IMC(peso, altura)
print(f"O seu imc é: {imc}")
situacao(imc)