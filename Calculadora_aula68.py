while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite um outro número: ')
    operador = input('Digite um operador (+-/*): ')

    numero_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except:
        numero_validos = None
    
    if numero_validos is None:
        print('um dos números que você digitou é invalido.')
        continue

    operadores_permitidos = '*/+-'
    if operador not in operadores_permitidos:
        print('Você digitou um operador inválido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas 1 operador')
        continue

    print('Realizando usa conta...')

    if operador == '+':
        print(num_1_float + num_2_float)
    
    elif operador == '-':
        print(num_1_float - num_2_float)
    
    elif operador == '/':
        print(num_1_float / num_2_float)
    
    elif operador == '*':
        print(num_1_float * num_2_float)

    sair = input("quer sair [s]im: ").lower().startswith('s')
    if sair == True:
        break
    
    
    

    



