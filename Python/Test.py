from datetime import datetime

def calcular_idade(ddn):

    hoje = datetime.now()

    idade = hoje.year - ddn.year

    return idade

def calcular_imc(peso, altura):

    return peso / (altura ** 2)

def main():

    nome = input('Digite seu nome completo: ')
    ddn_str = input('Digite sua data de nascimento (Dia/Mês/Ano): ')
    ddn = datetime.strptime(ddn_str, '%d/%m/%Y')
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))

    idade = calcular_idade(ddn)
    imc = calcular_imc(peso, altura)

    print(f'Saudações {nome}!')
    print(f'Você tem {idade} anos de idade')
    print(f'Seu Índice de Massa Corporal (IMC) é {imc}')

if __name__ == '__main__':
    main()
