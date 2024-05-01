num = 0

num = int(input('Digite qualquer numero: '))

if num > 0:

    num = num * 2

    print(f'Por ele ser positivo, o dobro desse número é {num}')

elif num < 0:

    num = num * 3

    print(f'Por ele ser negativo, o triplo desse número é {num}')

else:

    print('Pra que fazer isso?')
