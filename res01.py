
"""Obtém as informações básicas do usuário."""
nome = input("Digite o nome de usuário: ")
email = input("Digite o e-mail do usuário: ")
telefone = input("Digite o telefone do usuário: ")
    
# Dados do carro
autonomia_gasolina = 14  # km/l
autonomia_alcool = 12    # km/l
distancia_trabalho = 32 # km (ida)

"""Calcula o gasto mensal com gasolina e álcool, e a média de quilômetros rodados."""
# Distância diária de ida e volta
distancia_diaria = distancia_trabalho * 2

# Distância semanal e mensal
distancia_semanal = distancia_diaria * 5  # De segunda a sexta
distancia_mensal = distancia_semanal * 4  # Considerando 4 semanas por mês

# Consumo mensal de gasolina e álcool
consumo_gasolina = distancia_mensal / autonomia_gasolina
consumo_alcool = distancia_mensal / autonomia_alcool
    
# Preço por litro (exemplo de valores, substitua conforme necessário)
preco_gasolina_por_litro = float(input("Digite o preço da gasolina por litro (em reais): "))
preco_alcool_por_litro = float(input("Digite o preço do álcool por litro (em reais): "))

# Gasto mensal com gasolina e álcool
gasto_mensal_gasolina = consumo_gasolina * preco_gasolina_por_litro
gasto_mensal_alcool = consumo_alcool * preco_alcool_por_litro

print(30*'_')
# Informações do usuário
print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"Telefone: {telefone}")

# Resultados
print(f"\nGasto mensal com gasolina: R$ {gasto_mensal_gasolina:.2f}")
print(f"Gasto mensal com álcool: R$ {gasto_mensal_alcool:.2f}")
print(f"Média de quilômetros rodados mensalmente: {distancia_mensal:.2f} km")
print(f"Consumo Gasolina: {consumo_gasolina:.2f}L")
print(f"Consumo Alcool: {consumo_alcool:.2f}L")


