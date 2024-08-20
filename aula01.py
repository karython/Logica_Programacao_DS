print('Ola Mundo')

nome = 'Karython'
idade = 25 
peso = 85.8
altura = 1.75
instrutor = True

# FIXME: Visualizando os tipos de dados

# FIXME: Entrada de dados

sobrenome = input('Digite o seu sobrenome: ') 

print(type(sobrenome))

#convertendo o valor do input

idade = input('digite sua idade: ')
idade = int(idade)
print(type(idade))

ano =  int(input('em qual ano estamos: '))
print(type(ano))

if ano > 2024:
    print('dentro do if')

'''
    # TODO: Atividade
    Receber: nome, cpf, data de nascimento
    imprima: todos os dados e o seus tipos já convertidos

'''