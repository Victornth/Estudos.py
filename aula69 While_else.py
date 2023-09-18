string = 'valorqualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break
    
    print(letra)
    i += 1
else:
    print('não encontrei espaço na string. ')
print('fora do while')