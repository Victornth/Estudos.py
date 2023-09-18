frase = 'olha só que, coisa interessante'
lista_palavras = frase.split(',')#divide a str e coloca em uma lista, no caso aqui divide na virugla, onde tem virgula ele divide 
print(lista_palavras)
#para cada indice na frase le printa
for i, frase in enumerate(lista_palavras):
    print(i)
    print(frase)
    