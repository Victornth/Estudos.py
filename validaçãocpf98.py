#cpf usuario
cpf_enviado_usuario = '111111111'.replace('.','').replace('-','').replace(' ','')
#primeiro numero do cpf
cpf_sort = cpf_enviado_usuario[:9]
i = 10
i2 = 11
soma_cpf = 0
somageral_2 = 0  

for item in cpf_sort:
    soma = int(item) * i
    i = i - 1
    soma_cpf += int(soma)

soma_cpf = soma_cpf * 10
resto_digito_1 = soma_cpf % 11
if resto_digito_1 > 9:
    resto_digito_1 = 0
else:
    resto_digito_1 = resto_digito_1
 
#calculo digito 2
cpf_sort_2 = cpf_sort + str(resto_digito_1)
soma2 = 0
for item_2 in cpf_sort_2:
    soma2 = int(item_2) * i2
    i2 = i2 - 1
    somageral_2 += int(soma2)
somageral_2 = ((somageral_2 *10) % 11)

cpf_gerado_pelo_calculo = f'{cpf_sort}{resto_digito_1}{somageral_2}'
print(cpf_gerado_pelo_calculo)

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f"{cpf_enviado_usuario} é valido")
else:
    print(f'{cpf_gerado_pelo_calculo}é Cpf invalido')
