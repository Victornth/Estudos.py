import os
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativa = 0
while True:
    numero_tentativa += 1
    letra_digitada = input("Digite uma letra: ")
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas+= letra_digitada
    
    palavra_formada=''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        print('você ganhou!!')
        print(f'A palavra secreta era {palavra_secreta}')
        print(f'o seu numero de tentativas foi: {numero_tentativa}')
        letras_acertadas = ''
        numero_tentativa = 0


    

            
            


    