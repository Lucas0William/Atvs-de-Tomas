# Programa 12 casas

# Entrada

#     Nome Completo
#     Data de nascimento (formato dia mês ano)
#     Altura
#     Peso
#     Sexo (Masculino ou Feminino)

# Fazer: Calcular IMC e descobrir signo

# Saída

#     FULANO cavaleiro/amazona de SIGNO
#     Masculino=cavaleiro
#     Feminino=amazona

# Informar se pode ou não ser um cavaleiro (IMC precisa ser o peso ideal)

#==============================================================================

    # Aquário: de 21 de janeiro a 18 de fevereiro;
    # Peixes: de 19 de fevereiro a 20 de março;
    # Áries: de 21 de março a 20 de abril;
    # Touro: de 21 de abril a 20 de maio;
    # Gêmeos: de 21 de maio a 20 de junho;
    # Câncer: de 21 de junho a 22 de julho;
    # Leão: de 23 de julho a 22 de agosto;
    # Virgem: de 23 de agosto a 22 de setembro;
    # Libra: de 23 de setembro a 22 de outubro;
    # Escorpião: de 23 de outubro a 21 de novembro;
    # Sagitário: de 22 de novembro a 21 de dezembro;
    # Capricórnio: de 22 de dezembro a 20 de janeiro;
   
def signo(dia, mes):

    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):

        return "Aquário"
    
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):

        return "Peixes"
    
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):

        return "Áries"
    
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):

        return "Touro"
    
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):

        return "Gêmeos"
    
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):

        return "Câncer"
    
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):

        return "Leão"
    
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):

        return "Virgem"
    
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):

        return "Libra"
    
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):

        return "Escorpião"
    
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):

        return "Sagitário"
    
    else:

        return "Capricórnio"

nome = input("Digite seu nome completo: ")

data_nascimento_str = input("Digite sua data de nascimento (formato: dia mês ano - ex: DD MM AAAA): ")

dia, mes, ano = map(int, data_nascimento_str.split())

altura = float(input("Digite sua altura (em metros): "))

peso = float(input("Digite seu peso (em quilogramas): "))

sexo = input("Digite seu sexo (Masculino ou Feminino): ").lower()

imc = peso / (altura ** 2)

casa = signo(dia, mes)

if imc >= 18.5 and imc <= 24.9:

    cavaleiro_amazona = "cavaleiro" if sexo == "masculino" else "amazona"

    print(f"Parabéns {nome}, você será um {cavaleiro_amazona} de {casa}!")

else:

    print(f"Infelizmente {nome} não pode ser um cavaleiro, pois seu IMC não está dentro do ideal.")
