# Dicionário para armazenar os usuários
usuarios = {}

# Loop para o menu de opções
while True:
    print("\n--- Sistema de Cadastro de Usuários ---")
    print("1. Cadastrar Usuário")
    print("2. Listar Usuários")
    print("3. Remover Usuário")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    # Cadastrar usuário
    if opcao == '1':
        nome = input("Digite o nome do usuário: ")
        senha = input("Digite a sua senha do usuário: ")
        email = input("Digite o e-mail do usuário: ")
        usuarios[nome] = {"nome": nome, "senha": senha, 'email':email}

        print(f"Usuário {nome} cadastrado com sucesso!")
        
    # Listar usuários
    elif opcao == '2':
        if usuarios:
            print("\n--- Lista de Usuários Cadastrados ---")
            for email, dados in usuarios.items():
                print(f"Nome: {dados['nome']}, Senha: {dados['senha']},
                       E-mail: {dados['email']}")
        else:
            print("Nenhum usuário cadastrado.")     

    # Remover usuário
    elif opcao == '3':
        nome_remove = input('Digite o nome que deseja remover: ')
        if nome_remove in usuarios:
            del usuarios[nome_remove]
            print('Usuario removido com sucesso!')
        else:
            print('Usuario nao encontrado!')


    
    # Sair do sistema
    elif opcao == '4':
        print("Saindo do sistema...")
        break
    
    # Opção inválida
    else:
        print("Opção inválida. Tente novamente.")
