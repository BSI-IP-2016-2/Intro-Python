palavra = "BRASIL" 
acertos = 0 
erros = 6
qtdErros = 0
palavraf = "_" * len(palavra) #Define uma variável para receber as modifica��es e apresentar os acertos quando existirem

while (erros > 0): #Entra num loop para contar acertos e erros
    letra = input("Digite uma letra: ").upper() #Digita a palavra e transforma em mai�scula pra evitar problemas de case-sensitive
    if(palavra.find(letra) != -1): #Se encontrar a palavra adiciona +1 em acerto e entra no for
        for i in range(len(palavra)): 
            if (letra in palavra[i]):
                '''
                Ele vai procurar pelo length da palavra até� que a condicional "if" seja satisfeita.
                Se ela for satisfeita, ele vai então pegar a "palavraf" e criar uma nova string
                Onde ser� adicionar a parte encontrada em "palavra" na mesma �área de "palavraf" + a letra encontrada em "palavra"
                + a "palavraf" a partir da letra adicionada + 1 espaço "_" pra fusionar os dois.
                '''
                palavraf = palavraf[:i] + palavra[i] + palavraf[i+1:]
        acertos += 1
        if(acertos <= 5):
            print("A palavra é: %s" % (palavraf))
    elif(palavra.find(letra) == -1): #Se não encontrar, adiciona uma quantidade de erro pra contar quantos já foram feitos
        #E decrementa um erro pra contar até 0 e dar fim de jogo
        qtdErros += 1
        print("Você errou pela %d" % (qtdErros) + "ª vez. Tente novamente")
        erros -= 1
    if(acertos == len(palavra)):
        print("Você venceu! :D A palavra era: %s" % (palavra))
        break
else:
    print("Voc� perdeu :(")