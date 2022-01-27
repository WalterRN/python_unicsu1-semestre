'''
Calcular através de um programa que leia a categoria de 
um produto e determine o preço pela tabela: 
Categoria 1 valor de R$ 10,00; 
Categoria 2 valor de R$ 18,00; 
Categoria 3 valor de R$ 23,00;
Categoria 4 valor de R$ 26,00 e 
Categoria 5 valor de R$ 31,00.
'''

categoria = int(input("Digite a categoria do produto:"))
if categoria == 1:
    preço = 10
else:
    if categoria == 2:
        preço = 18
    else:
        if categoria == 3:
             preço = 23
        else:
            if categoria == 4:
                preço = 26
            else:
                if categoria == 5:
                    preço = 31
                else:
                    print("Categoria inválida, digite um valor entre 1 e 5!")
                    preço = 0 
print("O preço do produto é: R$%6.2f" % preço) 
                                           