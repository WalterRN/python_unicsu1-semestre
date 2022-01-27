def calcularIMC(pPeso, pAltura):
    imc = pPeso / (pAltura**2)
    return imc

def classificarIMC(pImc):
    if pImc < 18.5:
        print("Classificação: Desnutrição")
    elif pImc < 25:
        print("Classificação: Peso Normal")
    elif pImc < 30:
        print("Classificação: Sobrepeso")
    elif pImc < 35:
        print("Classificação: Obesidade I")
    else:
        print("Classificação: Obesidade II")

def menu():
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = calcularIMC(peso, altura)
    print(f"O seu imc é: {imc}")
    classificarIMC(imc)

menu()