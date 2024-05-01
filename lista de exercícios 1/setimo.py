nota1 = 0
nota2 = 0
nota3 = 0

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + (nota2 * 2) + (nota3 * 3)) / 6

if media >= 90:

    print(f'Esse aluno foi nota "A" e recebeu status APROVADO! com média {media:.2f}')

elif media >= 75 and media < 90:

    print(f'Esse aluno foi nota "B" e recebeu status APROVADO! com média {media:.2f}')

elif media >= 60 and media < 75:

    print(f'Esse aluno foi nota "C" e recebeu status APROVADO! com média {media:.2f}')

elif media >= 40 and media < 60:

    print(f'Esse aluno foi nota "D" e recebeu status REPROVADO! com média {media:.2f}')

elif media < 40:

    print(f'Esse aluno foi nota "E" e recebeu o status REPROVADO! com média {media:.2f}')
