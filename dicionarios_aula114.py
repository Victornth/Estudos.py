pessoa = {
    'nome': 'Victornt',
    'sobrenome':'hugo',
    'idade':22,
    'altura':1.77,
    'endereços':[
        {'rua':'tal tal','numero':123},
        {'rua':'tal tal','numero':321},
    ],
    }

print(pessoa['nome'])
print(pessoa['sobrenome'])
print()


for chave in pessoa:
    print(chave, pessoa[chave])