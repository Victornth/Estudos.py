nome = input('Digite seu nome para ser adicionado (*) no meio do seu nome:')

tamanho_nome = len(nome)

print(f'{tamanho_nome}')

contador = 0
novo_nome = ''

while contador < tamanho_nome:
    nova_string = '*' + nome[contador]
    novo_nome += nova_string
    print(f'{nova_string}',end="")
    
    contador += 1
print(f'\n{novo_nome}')
   
