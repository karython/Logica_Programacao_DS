nome = 'Karython'
idade = 25


#peso = input('Digite seu peso: ')

num1 = input('Digite o primeiro numero: ')
num1 = int(num1)

num2 = int(input('Digite o segundo numero: '))

# operadores matematicos
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
divi = num1 / num2
divi_inteira = num1 // num2
expo = num1 ** num2
modulo = num1 % num2 # resto da divisão

# FIXME: Operadores comparativos

print('Operadores comparativos')
print(num1 > num2)  # maior que
print(num1 < num2)  # menor que
print(num1 == num2) # igualdade
print(num1 != num2) # diferente
print(num1 <= 100)  # menor ou igual

print(num1 <= 100 and num2 <=100 or (num1 + num2) > 100)


# FIXME: Operadores matemáticos
print('Operadores matemáticos no print')
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)

# FIXME Atribuição de valores
num1 += 1
num1 -= 1
num1 /= 1
num1 *=1

print(f'Soma: {soma}')
print(f'Subtração: {sub}')
print(f'Multiplicação: {mult}')
print(f'Divisão: {divi}')
print(f'Divisão formatada: {divi:.2f}')
print(f'Divisão inteira: {divi_inteira}')
print(f'Exponenciação: {expo}')
print(f'Resto da divisão: {modulo}')
print()
print(f'O numero digitado + 1 é: {num1}')


# Atividade 01:
'''
    Criar um sistema para receber o nome, idade, peso, altura
    Converter a idade para receber somente numeros inteiros
    Imprimir os tipos de dados
    Imprimir todas as informações concatenadas usando f string
'''
# Atividade 02:
'''
    Declare 2 variáveis, cada uma com um valor, e some os resultados concatenados a um texto.
    Crie um sistema onde o usuário irá inserir dois valores, guarde cada valor em variáveis, em seguida vocês irão realizar as 4 operações básicas de matematica (+; -; *, /) e mostrar esses resultados na tela, tambem concatenados a um texto indicativo de cada operação.
    Crie um sistema que receba o nome do usuário, a idade so podendo aceitar numero inteiro, em seguida mostre o nome e idade do usuario e peça que ele digite 2 números para que sejam somados. Mostrar por último a soma realizada para o usuário.

'''
# Atividade 03:
'''
    Crie um sistema que receba 2 valores do usuario, sem deixar restrito a entrada de dados, trate os dados de entrada e realize a soma dos valores.
    Crie um sistema que calcule a media de 5 notas dos alunos, usando comandos de entrada de dados e tratando as entradas dos usuarios, sem usar restrição.
'''
