A = 0
B = 0
C = 0

A = int(input('Digite um numero: '))
B = int(input('Digite outro numero: '))

if A > B:

    C = A + B

    print(f'O resultado foi {C}, e o caminho utilizado foi o de soma pois\nO primeiro numero foi maior')

elif A < B:

    C = A * B

    print(F'O resultado foi {C}, o caminho utilizado foi o de multiplicação \nPois o segundo numeral foi o maior')

elif A == B:

   print('Os dois numeros são iguais, bora, use direito o código')

else:

    pass
    