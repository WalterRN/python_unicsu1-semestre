def calcularIMC(pPeso, pAltura):
    imc = pPeso / (pAltura**2)
    return imc

def classificarIMC(pImc):
    if pImc < 18.5:
        return "Desnutrição"
    elif pImc < 25:
        return "Peso Normal"
    elif pImc < 30:
        return "Sobrepeso"
    elif pImc < 35:
        return "Obesidade I"
    else:
        return "Obesidade II"

def menu():
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = calcularIMC(peso, altura)
    classificacao = classificarIMC(imc)
    print(f"O seu imc é: {imc} e sua classificação é: {classificacao}")
    

menu()