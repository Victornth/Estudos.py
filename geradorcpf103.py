import random
import sys

for k in range(100):
  
    cpf_enviado_usuario = ''
    #primeiro numero do cpf
    for c in range(9):
        cpf_enviado_usuario += str(random.randint(0,9))
    

    i = 10 
    soma_cpf = 0

    for item in cpf_enviado_usuario:
        soma = int(item) * i
        i = i - 1
        soma_cpf += int(soma)

    resto_digito_1 = ((soma_cpf * 10)%11)
    resto_digito_1 = resto_digito_1 if resto_digito_1 <= 9 else 0
    
    
    #calculo digito 2
    i2 = 11
    somageral_2 = 0  
    cpf_sort_2 = cpf_enviado_usuario + str(resto_digito_1)
    soma2 = 0
    for item_2 in cpf_sort_2:
        soma2 = int(item_2) * i2
        i2 = i2 - 1
        somageral_2 += int(soma2)
    somageral_2 = ((somageral_2 *10) % 11)
    somageral_2 = somageral_2 if somageral_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{cpf_enviado_usuario}{resto_digito_1}{somageral_2}'
    print(cpf_gerado_pelo_calculo)
    
