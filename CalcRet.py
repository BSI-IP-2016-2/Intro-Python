x, y = (0,)*2 #Define as variáveis iniciais X e Y como 0
while True: #Diz pra o código que enquanto estiver T ele continuará executando essa parte
    try: 
        x = int(input("Digite a base: ")) #Mostra pro usuário o input e tenta verificar se o que foi digitado é um int(inteiro)
    except ValueError: #Caso não seja um inteiro ele mostra uma exceção jogando uma mensagem pro usuário
        print("Você não pode deixar o espaço vazio ou digitou uma letra") #Mostra a mensagem de erro
        continue #Mantém o loop e joga de volta pro "try"
    else: #Caso o número inteiro seja identificado, ele para o loop e prossegue o código.
        break
while True: #Faz o mesmo do de cima só que para o segundo número.
    try:
        y = int(input("Digite a altura: "))
    except ValueError:
        print("Você não pode deixar o espaço vazio ou digitou uma letra")
        continue
    else:
        break #Terminar o loop e prossegue
if x > 0 and y > 0: #Verifica se o número digitado foi maior que zero. Se sim, ele prossegue pro cálculo
    print(x * y) #Cálcula o resultado e mostra na tela.
