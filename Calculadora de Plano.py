print('Boas-vindas, Davi Wellington Ribeiro da Silva!')
# Usuario entra com os dados
valorBase = float(input('Qual é o valor base do Plano? R$ '))
idade = float(input('Qual é a sua idade? '))

# Programa faz o cálculo mensal conforme a idade 
if (idade >= 0 and idade < 19):
    valorMensal = (valorBase * (100/100))
    print(f'O valor mensal que você pagará será de R$ {valorMensal}')
else:
    if (idade >= 19 and idade < 29):
        valorMensal = (valorBase * (150/100))
        print(f'O valor mensal que você pagará será de R$ {valorMensal}')
    elif (idade >= 29 and idade < 39):
        valorMensal = (valorBase * 225/100)
        print(f'O valor mensal que você pagará será de R$ {valorMensal}')
    elif (idade >= 39 and idade < 49):
        valorMensal = (valorBase * 240/100)
        print(f'O valor mensal que você pagará será de R$ {valorMensal}')
    elif (idade >= 49 and idade < 59):
        valorMensal = (valorBase * 350/100)
        print(f'O valor mensal que você pagará será de R$ {valorMensal}')
    elif (idade >= 59 ):
        valorMensal = (valorBase * 600/100)
        print(f'O valor mensal que você pagará será de R$ {valorMensal} reais')
