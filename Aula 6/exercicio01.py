'''Em uma escola, um aluno aprovará uma disciplina se a média das três
avaliações for maior ou igual que 6 e o percentual de presença maior ou
igual que 75%. Também aprovaria se a média for maior que 8, independente
da frequência. Em qualquer outro caso o aluno estará reprovado.
'''
#entrada de dados
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a primeira nota: "))
nota3 = float(input("digite a primeira nota: "))
frequencia = float(input("digite a frequência as aulas: "))

#processamento dos dados
media = (nota1 + nota2 + nota3)/3

if media >= 6.0 and frequencia >= 75.0:
    print(f"o aluno está aprovado com média {media} e frequência {frequencia}%!!!")
else:
    if media > 8.0:
        print(f"o aluno está aprovado com média {media} e frequência {frequencia}%!!!")
    else:
        print(f"o aluno está reprovado com média {media} e frequência {frequencia}%!!!")