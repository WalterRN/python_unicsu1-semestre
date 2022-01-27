'''Escreva uma função que receba a base e a altura de um triângulo e 
retorne sua área:
(A=(base x altura)/2)
Valores esperados:
● Área_triangulo(6,9) == 27
● Área_triangulo(5,8) == 20
'''

b = float(input("Digite o perimetro número"))
a = float(input("Digite o perimetro número"))

def area(b,a):
    resultado = (b * a) /2
    return resultado
print(f"A área de quadrado é: {area(a)}")