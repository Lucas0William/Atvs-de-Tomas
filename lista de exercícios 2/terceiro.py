pessoa = 0
mv = 1
mn = 1000
for i in range (0, 12):

    pessoa = int(input('Digite sua idade: '))

    if pessoa > mv:

        mv = pessoa

    if pessoa < mn:

        mn = pessoa

print(f'O mais velho tem {mv} anos e o mais novo tem {mn} anos ')
