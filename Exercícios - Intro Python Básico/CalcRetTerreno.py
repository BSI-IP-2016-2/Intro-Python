x, y = (0,)*2 #Define as variáveis iniciais X e Y como 0
while True: #Diz pra o código que enquanto estiver T ele continuará executando essa parte
    try: 
        x = int(input("Digite a largura: ")) #Mostra pro usuário o input e tenta verificar se o que foi digitado é um int(inteiro)
    except ValueError: #Caso não seja um inteiro ele mostra uma exceção jogando uma mensagem pro usuário
        print("Você não pode deixar o espaço vazio ou digitou uma letra")
        continue #Mantém o loop caso não identifique um inteiro e joga de volta pro "try" pra que o usuário possa digitar de novo
    else: #Caso o número inteiro seja identificado, ele para o loop e prossegue o código.
        break #Diz pro código que ele não precisa mais ficar no loop e pode prosseguir
while True: #Faz o mesmo do de cima só que para o segundo número.
    try:
        y = int(input("Digite o comprimento: "))
    except ValueError:
        print("Você não pode deixar o espaço vazio ou digitou uma letra")
        continue
    else:
        break #Diz pro código que ele não precisa mais ficar no loop e pode prosseguir
xy = x * y #Cálcula o resultado e armazena na variável "xy"
if int(x) > 0 and int(y) > 0: #Verifica se o número digitado foi maior que zero. Se sim, ele prossegue pro cálculo
    print('A área do seu terreno é: %d' % (xy)) #Mostra o resultado na tela junto a um texto
else:
    print('Medida para cálculo inexistente!')
