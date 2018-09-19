def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_', ]

    print(letras_acertadas)

    enforcou = False
    acertou = False

    while(not enforcou  and not acertou):
        chute = input('Qual a letra? ').strip()#


        index = 0
        for letra in palavra_secreta:
            if (chute.lower() == letra.lower()):#lower() deixa todas strings minuscalas
                letras_acertadas[index]=letra
            index = index+1

        print (letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
