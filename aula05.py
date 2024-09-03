
#lista = ['gomes', 10, True, 1.60]

lista1 = [1,2,3,4,5,6,7,8,9,10]

#print(lista1[0])
#print(lista1[2:])
# indices negativos sao tratados de maneira especial, o -1 é considerado o ultimo elemento
#print(lista1[-1])

lista_int = [10,5,3,49,8,3,4,9,42,15,16,13,11,20]
print(lista_int)
lista_int.sort()

print(lista_int)
lista_int.sort(reverse=True)

print(lista_int)
print(f'Lista ordenada direto no print: {sorted(lista_int, reverse=True)}')

# remove, pop, del

nomes = ['gomes', 'oliveira', 'joao', 'pedro', 'jose', 'dias', 'ronaldo', 'kauan', 'dias']
print(nomes)

# remove a primeira ocorencia da lista
nomes.remove('dias')
print(nomes)

# remove um item de acordo com o indice informado
nomes.pop(1)
nomes.pop(-2)
print(nomes)


# remove mais de um elemento da lista
del nomes[5:]
print(nomes)


lista_nomes = []

novo_nome = input("Digite um novo nome: ")
lista_nomes.append(novo_nome)

print(lista_nomes)