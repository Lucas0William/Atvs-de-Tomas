celsius = 0
Fah = 0
kelvin = 0
decision = 0

celsius = float(input('Digite a temperatura (em Celsius): '))

Fah = (celsius * 1.8) + 32
kelvin = celsius + 273

print('''Qual opção deseja?
      
      [1] Celsius para Kelvin
      [2] Celsius para Fahrenheit
      
      ''')
decision = int(input(':> '))

if decision == 1:

    print(f'A temperatura informada ({celsius}°) convertida para Kelvin, será de {kelvin}°')

elif decision == 2:

    print(f'A temperatura informada ({celsius}°) converida para Fahrenheit, será {Fah}')

else:

    print('Decisão não reconhecida, tente novamente.')
