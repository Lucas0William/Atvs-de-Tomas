num = int(input('Digite o numero que deseja tranformar em binário: '))

binario = str(bin(num)[2::])

if num < 0:

    print('Não é possivel pois o número é negativo')

if num >= 0:

    print(f'O numero binario para {num} é {binario}')
