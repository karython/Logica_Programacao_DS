'''
Conteudo:
            - in ok
            - insert ok
            - append ok
            - lista[indice] = valor substituido ok
            - remove ok
            - if else elif
'''

lista = [1,45,23,12,11,6,8,4,34,19,14]

lista.sort()
lista.sort(reverse=True)
print(f'Lista ordena {lista}')

lista.remove(12)
lista.pop(5)
del lista[2:5]

nome = 'gomes'
lista.append(nome)
print(lista)

# isnerção
lista.insert(2, 'oliveira')
print(lista)

# substituicao
lista[2] = 'karython'
print(lista)

print('gomes' in lista)

if 'gomes' in lista:
    # esse bloco só sera executado quando a condição é true
    print('Sim, o gomes esta na lista')
else:
    # esse bloco só sera executado quando a condição é false
    print('Não, o gomes não está na lista')

notas = []

print(20*'-', ' BOLETIM ESCOLAR ',20*'-')
numero_usuario1 = int(input('Digite uma nota: '))
notas.append(numero_usuario1)

numero_usuario2 = int(input('Digite uma nota: '))
notas.append(numero_usuario2)

numero_usuario3 = int(input('Digite uma nota: '))
notas.append(numero_usuario3)

numero_usuario4 = int(input('Digite uma nota: '))
notas.append(numero_usuario4)

numero_usuario5 = int(input('Digite uma nota: '))
notas.append(numero_usuario5)

# len conta a quantidade de elementos dentro de uma lista
quantidade_notas = len(notas)

# sum irá somar todos os valores da lista
soma = sum(notas)

media = soma / quantidade_notas

print(f'A notas são: {notas}')
print(f'A quantidade de notas: {quantidade_notas}')
print(f'A soma de todas as notas: {soma}')
print(f'A média: {media}')

'''
    #TODO: Situação
    Aprovado >= 7
    Recuperação >= 5
    Reprovado  
'''
if media >= 7:
    print(f'Aprovado com média {media}')

elif media >=5:
    print(f'Recuperação com média {media}')

else:
    print(f'Reprovado com média {media}')

