### Funções em Python

**Objetivo**: Nesta aula, vamos aprender o conceito de funções em Python, como criá-las, chamá-las e usá-las para tornar nosso código mais organizado e eficiente.

#### 1. **O que são Funções?**

Funções são blocos de código reutilizáveis que executam uma tarefa específica. Elas permitem dividir um programa em partes menores, o que facilita a manutenção, leitura e reutilização do código. Além disso, ajudam a evitar a repetição de código.

- **Por que usar funções?**
  - Reduzem a duplicação de código.
  - Facilitam a manutenção.
  - Tornam o código mais legível.
  - Ajudam na organização lógica do programa.

#### 2. **Sintaxe Básica de Funções**

Em Python, a definição de uma função segue a seguinte estrutura:

```python
def nome_da_funcao(parametros_opcionais):
    # Bloco de código
    return valor_opcional
```

- `def` é a palavra-chave usada para definir a função.
- `nome_da_funcao` é o nome que damos à função.
- `parametros_opcionais` são os valores que a função pode receber (opcional).
- O código dentro da função é indentado.
- `return` é opcional, mas pode ser usado para retornar um valor da função.

#### 3. **Exemplo Prático**

Vamos criar uma função simples que recebe dois números e retorna a soma deles.

```python
def somar(a, b):
    resultado = a + b
    return resultado
```

Agora, podemos chamar essa função em nosso código:

```python
resultado = somar(5, 3)
print(f"O resultado da soma é: {resultado}")
```

#### 4. **Funções Sem Retorno**

Nem toda função precisa devolver um valor. Às vezes, queremos apenas que a função execute uma ação, como exibir uma mensagem.

```python
def mensagem():
    print("Olá, esta é uma mensagem dentro de uma função!")
```

Quando chamamos `mensagem()`, ela simplesmente imprime o texto na tela.

#### 5. **Parâmetros e Argumentos**

Funções podem receber valores de entrada, chamados parâmetros. Quando chamamos a função, passamos argumentos para esses parâmetros.

- **Parâmetros**: variáveis definidas na assinatura da função.
- **Argumentos**: valores que passamos ao chamar a função.

Exemplo com parâmetros:

```python
def cumprimentar(nome):
    print(f"Olá, {nome}!")
```

Chamando a função:

```python
cumprimentar("João")
```

#### 6. **Funções com Vários Parâmetros**

Funções podem receber mais de um parâmetro:

```python
def multiplicar(a, b):
    return a * b
```

Ao chamar a função, passamos dois argumentos:

```python
resultado = multiplicar(4, 5)
print(f"O resultado da multiplicação é: {resultado}")
```

#### 7. **Valores Padrão para Parâmetros**

Podemos definir valores padrão para os parâmetros. Assim, se o argumento não for fornecido, o valor padrão será usado.

```python
def saudacao(nome="visitante"):
    print(f"Bem-vindo, {nome}!")
```

Se chamarmos `saudacao()` sem passar nenhum argumento, o valor "visitante" será usado:

```python
saudacao()  # Saída: "Bem-vindo, visitante!"
```

#### 8. **Funções Recursivas**

Funções podem chamar a si mesmas. Isso é chamado de recursão. Vamos ver um exemplo clássico, o cálculo de fatorial:

```python
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)
```

Chamando a função para calcular o fatorial de 5:

```python
print(f"O fatorial de 5 é: {fatorial(5)}")
```

#### 9. **Funções Anônimas (Lambda)**

Python oferece uma maneira de criar funções anônimas usando a palavra-chave `lambda`. Essas funções são úteis para operações simples e rápidas.

Exemplo de função lambda para somar dois números:

```python
soma = lambda x, y: x + y
print(soma(2, 3))
```

#### 10. **Conclusão e Atividade Prática**

**Resumo**: Funções são essenciais para estruturar bem o código e torná-lo mais modular e reutilizável. Hoje, vimos como definir, chamar e usar funções com parâmetros e retorno, além de funções recursivas e lambdas.

**Atividade Prática**:
1. Crie uma função que receba três notas de um aluno e retorne a média.
2. Crie uma função que verifique se um número é par ou ímpar.
3. Crie uma função que receba uma lista de números e retorne apenas os números pares.

