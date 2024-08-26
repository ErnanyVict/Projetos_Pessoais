
while True:
        palavra = 'perfume' 
        palavra_secreta = len(palavra) * '*'
        tentativas = 0
        letras_achadas = ''
        palavra_achada = ''
        print(f'Palavra: {palavra_secreta}')
        while True:
            letra = input('Digite uma letra: ')
            tentativas += 1
            if len(letra) > 1:
                 print("Digite apenas UMA letra:")
                 continue
            if letra in palavra:
                letras_achadas += letra
                for letrasecreta in palavra:
                    if letrasecreta in letras_achadas:
                        palavra_achada += letrasecreta
                    else:
                         palavra_achada += "*"

            else:
                continue
            print(palavra_achada)
            if palavra_achada == palavra:
                print("VOCÊ GANHOU PARABÊNS!!")
                print(f'A palavra era: {palavra}')
                print(f'Tentativas: {tentativas}')
                break
            palavra_achada = ''
              
