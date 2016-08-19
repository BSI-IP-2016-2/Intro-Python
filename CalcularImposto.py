xCheque = 0 #Define a variável que representa o cheque que terá o imposto aplicado
while True:
    try:
        xCheque = float(input("Digite o salário: ")) #Espera para receber o valor do cheque e identificar se ele é float (inteiro ou decimal)
    except ValueError:
        print("Você não pode deixar o espaço vazio ou digitou uma letra")
        continue #Se tiver tudo certo ele continua, se não volta pro "try"
    else:
        break #Fecha o loop
Tax = xCheque * 0.3 #Faz o cálculo do imposto e armazena o valor na variável "Tax"
print('O salário final será: %d' % (Tax)) #Mostra a mensagem com a taxa que foi descontada
