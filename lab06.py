lista = []

nome1 = input('Digite um nome: ')
lista.append(nome1)

nome2 = input('Digite um nome: ')
lista.append(nome2)

lista.sort()

if nome1 and nome2 in lista:
    print(f'Sim, o {nome1} e o {nome2} está adicionado na lista')
else:
    print(f'Não, o {nome1} e o {nome2} não está na lista')

num1 = 10
num2 = 20

if num1 > num2:
    print('é maior')
else:
    print('é menor')
    if num1 < num2:
        print('é menor')
    else:
        print('é maior')
print('fim do bloco if else')


