aluno=input("Digite o seu nome: ")
nota1=float(input("Digite a nota 1: "))
nota2=float(input("Digite a nota 2: "))
nota3=float(input("Digite a nota 3: "))

média=(nota1+nota2+nota3)/3

if média >=9:
    print(aluno, "você está aprovado com excelente desempenho. ")
elif média >=7 and média <=8.9:
    print(aluno, "você está aprovado. ")
elif média >=5 and média <=6.9:
    print(aluno, "você está de recuperação. ")
else:
    print(aluno, "você está reprovado. ")
