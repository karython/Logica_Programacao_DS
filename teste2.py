# Lista para armazenar os produtos, onde cada produto será uma sublista com [nome, quantidade, preço]
inventario = []

# Loop principal do menu
while True:
    print("\n--- Menu de Gerenciamento de Inventário ---")
    print("1. Adicionar produto")
    print("2. Atualizar quantidade de produto")
    print("3. Listar todos os produtos")
    print("4. Calcular valor total do estoque")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        # Adicionar produto
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Digite o preço unitário: "))
        inventario.append([nome, quantidade, preco])
        print(f"Produto '{nome}' adicionado com sucesso!")

    elif opcao == '2':
        # Atualizar quantidade de produto
        nome = input("Digite o nome do produto que deseja atualizar: ")
        nova_quantidade = int(input("Digite a nova quantidade: "))
        
        encontrado = False
        for produto in inventario:
            if produto[0] == nome:
                produto[1] = nova_quantidade
                print(f"Quantidade do produto '{nome}' atualizada para {nova_quantidade}.")
                encontrado = True
                break
        
        if not encontrado:
            print(f"Produto '{nome}' não encontrado no inventário.")

    elif opcao == '3':
        # Listar todos os produtos
        if len(inventario) == 0:
            print("O inventário está vazio.")
        else:
            print("Produtos no inventário:")
            for produto in inventario:
                print(f"Nome: {produto[0]}, Quantidade: {produto[1]}, Preço: R$ {produto[2]:.2f}")

    elif opcao == '4':
        # Calcular o valor total em estoque
        valor_total = 0
        for produto in inventario:
            valor_total += produto[1] * produto[2]
        
        print(f"Valor total em estoque: R$ {valor_total:.2f}")

    elif opcao == '5':
        # Sair do programa
        print("Saindo do programa...")
        break

    else:
        # Opção inválida
        print("Opção inválida. Tente novamente.")
