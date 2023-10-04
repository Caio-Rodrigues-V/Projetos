#O que quero fazer?

# 1 - Gerar uma painel / lista de opção onde o usuario pode selecionar que tipo de operação ele deseja fazer

import math


def adi(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y

def potencia(x,y):
    return x ** y

def raiz(x):
    return math.sqrt(x)

def resto(x,y):
    return x % y

while True:
    

    print('[1] - Adição\n')
    print('[2] - Subtração\n')
    print('[3] - Multiplicação\n')
    print('[4] - Divisão \n')
    print('[5] - Potencia\n')
    print('[6] - Raiz Quadrada\n')
    print('[7] - Resto de um número\n')

    print('Agora digite os numeros que deseja calcular')

    print("O Que deseja calcular? ")

    option = str(input("Selecione de 1 a 7 para calcular seus numeros: "))

    if option not in ('1', '2', '3', '4', '5', '6', '7'):
        print('Opção inválida')
        continue

    n1 = float(input('Digite o primeiro numero que deseja operar: '))
    n2 = float(input('Digite o primeiro numero que deseja operar:  '))


    

    if option == '1':
        print('Resultado: ',adi(n1,n2))

    elif option == '2':
        print('Resultado: ',sub(n1,n2))

    elif option == '3':
        print('Resultado: ',mult(n1,n2))

    elif option == '4':
        print('Resultado: ',div(n1,n2))

    elif option == '5':
        print('Resultado: ', potencia(n1,n2))

    elif option == '6':
        print('Resultado: ',raiz(n1))

    elif option == '7':
        print('Resultado: ',resto(n1,n2))
    
    continuar = input('Deseja continuar calculando numeros? ')
    if continuar != 's':
        print('Fechando calculadora')
        break
