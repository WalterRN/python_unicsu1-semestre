salarioBruto = float(input("Digite o salario bruto: "))
 
def calcularInss (sb):
    return sb * 0.11
 
def calcularIR (sb):
    return sb * 0.27
 
def calcularSL(sb, inss, ir):
    print("Salario Liquido: ", sb - inss - ir)
 
inss = calcularInss(salarioBruto)
ir = calcularIR(salarioBruto)
calcularSL(salarioBruto, ir, inss)