import os
import time
lista_compra = []

while True:
    escolha = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air:").lower()
    if escolha == 'i':
        while True:
            lista_compra.append(input('Escreva oque deseja por na lista: '))
            print('item adicionado com sucesso')
            decisao = input('Deseja continuar adicionando?(S/N): ').strip().lower()
            if decisao == 'n':
                os.system('cls')
                break
            else:
                time.sleep(0.3)
                os.system('cls')
    elif escolha =='a':
        os.system('cls')

        for indice, nome in enumerate(lista_compra):
            print(indice, nome)

        remove = int(input('esolha o indice da lista para ser removido:'))
        if remove >= len(lista_compra):
            print('Não existe esse indice tente novamente')
        else:
            lista_compra.pop(remove)
            print('item removido com sucesso')
            time.sleep(0.5)
    elif escolha == 'l':
        os.system('cls')
        if len(lista_compra) == 0:
            print('Você não possui itens na lista') 
            time.sleep(2)
            os.system('cls')          
        else:
            for indice, nome in enumerate(lista_compra):
                print(indice, nome)
   
    elif escolha == 's':
        os.system('cls')
        print('Sua lista foi:')
        for indice, nome in enumerate(lista_compra):
            print(indice, nome)
        time.sleep(5)
        print('Você escolheu sair\n adeus!!! fofo :)')   
        break
   
    else:
        print('Você precisa escolher uma opção válida,dica: (apenas uma letra)')
        time.sleep(1)  
        os.system('cls')   