# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

def calcular():

    mensagem_inicial()

    define_operacao()

    escolha = int(input('\nDigite sua opção: '))

    primeiro_numero = int(input('Digite seu primeiro número: '))
    
    segundo_numero = int(input('Digite o segundo número: '))
    
    if (escolha == 1):
        resultado = primeiro_numero + segundo_numero
        print('O resultado da somatória é:', resultado)
    elif (escolha == 2):
        resultado = primeiro_numero - segundo_numero
        print('O resultado da subtração é:', resultado)
    elif (escolha == 3):
        resultado = primeiro_numero * segundo_numero
        print('O resultado da multiplicação é:', resultado)
    elif (escolha == 4):
        resultado = primeiro_numero / segundo_numero
        print('O resultado da divisão é:', resultado)
    else:
        print('Opção inválida!')
    
# Funções:
def mensagem_inicial():
    print('******************************')
    print('Bem-vindo ao Python Calculator')
    print('******************************')

def define_operacao():
    print('\nSelecione a operação que deseja realizar: ')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    
if(__name__ == '__main__'):
    calcular()