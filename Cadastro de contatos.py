print('Boas-vindas, Davi Wellington Ribeiro da Silva!')
# Lista para armazenar os contatos
lista_contatos = []
id_global = 5541023

# Função de entrada para o Usuario cadastrar contato
def cadastrar_contato(id):
    print('-------- CADASTRO DE CONTATO --------')
    print(f'Id do contato: {id_global}')
    nome = input('Qual é o nome do contato? ')
    atividade = input ('Qual é a atividade? ')
    telefone = input('Qual é o telefone? ')

# Cria um dicionário com os dados do contato
    contato = {
        'id': id,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
}

# adiciona uma copia na lista de contatos
    lista_contatos.append(contato.copy())
    print('Contato cadastrado com sucesso!')

# Função que consulta os contatos
def consultar_contatos():
    while True:
        print('-------- CONSULTAR CONTATOS -------')
        print('1 --> Consultar todos')
        print('2 --> Consultar por Id')
        print('3 --> Consultar por setor')
        print('4 --> Retornar ao menu')

        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            for contato in lista_contatos:
                print(contato)
        
        elif escolha == 2:
            id_busca = int(input('Digite o id do contato: '))
            encontrado = False
            
            for contato in lista_contatos:
                if contato['id'] == id_busca:
                    print(contato)
                    encontrado = True
            
            if not encontrado:
                print('Id não encontrado!')
        
        elif escolha == 3:
            atividade_busca = input('Digite a atividade: ')
            encontrado = False
            
            for contato in lista_contatos:
                if contato['atividade'] == atividade_busca:
                    print(contato)
                    encontrado = True
            
            if not encontrado:
                print('Nenhum contato encontrado!')
        
        elif escolha == 4:
            return
        
        else:
            print('Opção inválida!')

# Função para remover contato
def remover_contato():
    while True:
        print('------- REMOVER CONTATO -------')
        try:
            id_remover = int(input('Digite o id do contato que deseja remover: '))
        except ValueError:
            print('Id inválido')
            continue

        for contato in lista_contatos:
            if contato['id'] == id_remover:
                lista_contatos.remove(contato)
                return
        
        print('Id inválido. Tente novamente!')

# Menu principal do sistema
while True:
    print('\n---------- MENU PRINCIPAL ----------')
    print('1 --> Cadastrar Contato')
    print('2 --> Consultar Contato')
    print('3 --> Remover Contato')
    print('4 --> Encerrar Programa')

    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite um número válido!')
        continue

    if opcao == 1:
        cadastrar_contato(id_global)
        id_global += 1  
    
    elif opcao == 2:
        consultar_contatos()
    
    elif opcao == 3:
        remover_contato()
    
    elif opcao == 4:
        print('Programa encerrado.')
        break
    
    else:
        print('Opção inválida!')
