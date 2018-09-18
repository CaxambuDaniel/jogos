def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False

    while(not enforcou  and not acertou):
        chute = input('Qual a letra? ').strip()#strip() tira os espaços inseridos pelo usuario.

        index = 0
        for letra in palavra_secreta:
            if (chute.lower() == letra.lower()):#lower() deixa todas strings minuscalas para nao ter problemas com a comparação
                print('encontrei a letra {} na posição {}'.format(chute, index+1))
            index = index+1

        print ('jogando...')

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
