qntdR = int(input('Digite a quantidade de rodas: '))
peso = float(input('Digite o peso do veículo: '))
qntdP = int(input('Digite a quantidade de pessoas no veículo: '))

if qntdR <= 3:
    print('Você precisa de categoria A')

elif qntdR >= 4:

    if qntdP <= 8 and peso <= 3500:

        print('Você precisa de categoria B')

    elif peso > 3500 and peso <= 6000:

        print('Você precisa de categoria C')
    
    elif qntdP > 8:

        print('Você precisa de categoria D')

    elif peso > 6000:

        print('Você precisa de categoria E')
