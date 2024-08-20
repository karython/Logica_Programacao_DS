# Tipos de concatenação
# Concatenação com sinal (+)
num = int(input('Digite um numero inteiro: '))

# não possivel concatenar numero inteiro usando esse metodo, a menos que
# converta o numero inteiro em uma string
print('Ola, '+ str(num) +'. Seja bem-vindo!')
print(type(num))

# Concatenação com a (,)
print('O numero digitado é:',num)

# Concatenação com fstring (f)
print(f'O numero digitado é: {num} usando a concatenação "f"')

div = num / 3
# Usando format para formatação numérica
# limitando a quantidade de casas decimais
print(f'O resultado da divisao é: {div:.5f}')

'''
    Desenvolva um sistema que receba o cadastro do nome de usuario e as 
    suas informações basicas, como, email e telefone, em seguida, calcule
    o gasto de combustivel mensal, considerando que o carro que ele usa tem
    capacidade total de 55 litros. Na gasolina ele tem autonomia de 14km/l, já
    no alcool a autonomia é de 12km/l. Considere que de casa ao trabalho são 32km
    e ele precisa ir e voltar do trabalho de segunda a sexta. 
        - Qual será o gasto mensal (reais/litro) que o usuario terá no alcool e na gasolina? 
        - Qual á média de kilometros rodados mensalmente?
'''