num = int(input('Digite o numero que deseja saber a tabuada: '))

for i in range(0, 11):

    result = num * i
    
    print(num, 'x', i, '=', result)

    i += 1
