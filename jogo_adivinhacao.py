import random
import os

# recebe um numero aleatorio entre 0 e 100
numero_premiado = random.randint(0,100)
num_tentados = []
tentativas = 5



os.system('cls')

while True:
        ent_usuario = int(input('Digite um número: '))
        print()
        if ent_usuario == numero_premiado:
            print('Você ganhou!')
            break
        elif tentativas == 0:
            print(f'Você perdeu, o número premiado era {numero_premiado}')
            break
        
        else:
            print('Você não acertou o numero!')
            # adiciona o numero tentado na lista
            num_tentados.append(ent_usuario)
            tentativas -=1
            
            # Verifica se o numero digitado é maior ou menor
            if ent_usuario > numero_premiado:
                print('Digite um número menor!')
            else:
                print("Digite um número maior!")
      
print('Fim do jogo')
print(f'Voce tentou os numeros: {num_tentados}')
print(f'Você teve: {len(num_tentados)} tentativas')
