def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'banana'.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou  and not acertou):
        chute = input('Qual a letra? ').strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print('a palavra não possui a letra informada, voce possui mais {} tentativas '.format(6-erros))

        enforcou = (erros == 6)
        acertou = ('_' not in letras_acertadas)
        print (letras_acertadas)

    if(acertou == True):
        print('Voce acertou, a palavra era {}, parabens!!!'.format(palavra_secreta))
    else:
        print('voce gastou tadas as tentativas e não acertou, tente outra vez')
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
