# vp = Valor do produto
# fp = Forma de Pagamento
# qp = Quantidade de parcelas
# j = Juros
# vfj = Valor final com Juros 


vp = 0
fp = 0
vp = float(input('qual o preço do produto?: '))

print('''
        Qual sera a forma de pagamento?
               
        [1] A vista, Pix, Débito
        [2] Crédito a vista
        [3] Crédito parcelado
               
        ''')

fp = int(input(':> '))

if fp == 1:

    vp = vp * 0.9

    print(f'O preço final do produto ficará em R${vp}, pois recebeu 10% de desconto')

elif fp == 2:

    print(f'O preço do produto permace o mesmo, R${vp}')

elif fp == 3:

    qp = int(input('Quantas parcelas você deseja? '))

    j = vp * 0.1 * qp
    
    vfj = vp + j

    print(f'O preço final ficará em R${vfj}, pois foi parcelado em {qp} vezes')

