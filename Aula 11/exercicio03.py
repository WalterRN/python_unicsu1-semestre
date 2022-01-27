
'''Faça um programa com uma função chamada somaImposto. 
A função possui dois parâmetros formais: taxaImposto, 
que é a quantia de imposto sobre vendas expressa em porcentagem.  
Custo: que é o custo de um item antes do imposto. 
Criar a função e fazer o teste enviando valor para ela e imprimindo
resultado'''


def somaImposto(taxaimposto, custo):
    return (0.01*taxaimposto) * custo

def menu():
    taxa = float(input("Digite um percentual de imposto: "))
    custo = float(input("Digite o valor do custo: "))
    resultado = somaImposto(taxa, custo)
    print(f"O valor do imposto é: {resultado}")

menu()