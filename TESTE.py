
import random
import sys

for x in range(1000):
    cpf_enviado_usuario =''
    for i in range(9):
        cpf_enviado_usuario += str(random.randint(0,9))

    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in cpf_enviado_usuario:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = cpf_enviado_usuario + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{cpf_enviado_usuario}{digito_1}{digito_2}'
    print(cpf_gerado_pelo_calculo)