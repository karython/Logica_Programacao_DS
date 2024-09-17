import os
lista_usuario = []

while True:
    print()
    print(30*'*', 'Menu', 30*'*')    
    print('1. Cadastrar usuario.')
    print('2. Listar Usuario.')
    print('3. Excluir usuario.')
    print('4. Buscar pelo nome.')
    print('5. Inserir em uma posicao')
    print('6. Sair')
    print(66*'*')
    print()

    opcao = input('Digite a opcao desejada: ')

    # Cadastrar usuario
    if opcao == '1':
        nome = input('Digite o nome que deseja cadastrar: ').upper()

        if nome != '':
            lista_usuario.append(nome)
            print(f'Usuario {nome} cadastrado com sucesso!')
        else:
            print('Digite algum valor!')
    
    #listar usuario
    elif opcao == '2':
        for i, n in enumerate(lista_usuario):
            print(f'{i + 1}° {n}')


    #Excluir usuario
    elif opcao == '3':

        for i, n in enumerate(lista_usuario):
            print(f'{i}: {n}')

        posicao = int(input('Digite o numero do usuario que deseja excluir: '))
        
        for j, _ in enumerate(lista_usuario):
            if j == posicao:
                lista_usuario.pop(j)
                print(f'Usuario da posicao {j} foi removido!')

        '''
        for i in lista_usuario:
            if nome == i:
                lista_usuario.remove(i)
                print('Usuario removido com sucesso')
        '''
    # buscar pelo nome
    elif opcao == '4':
        nome_buscar = input('Digite o nome que deseja buscar na lista: ').upper()

        if nome_buscar != '':
            for i in lista_usuario:
                if i == nome_buscar:
                    print(i)
      
    # inserir em uma posicao
    elif opcao == '5':
        novo_nome = input('Digite o nome que deseja inserir: ').upper()
        posicao_nome = int(input('Digite a posicao que deseja inserir: '))

        # Correcao da posicao
        posicao_nome -=1
        if posicao_nome >= 0 and posicao_nome <= len(lista_usuario):
            lista_usuario.insert(posicao_nome, novo_nome)
        else:
            print('Posição invalida!')


    # Sair
    elif opcao == '6':
        print('Saindo do Sistema!')
        break

    else:
        print('Digite uma opcao válida!')


