xSal = 0 #Define o salário que será digitado
while True:
    try:
        xSal = float(input("Digite o salário: ")) #Procura saber se ele é float (inteiro ou decimal)
    except ValueError:
        print("Você não pode deixar o espaço vazio ou digitou uma letra")
        continue #Senão for continua no loop.
    else:
        break #Se for ele passa pro próximo código
xSalFinal = (xSal * 0.2) + xSal #Faz o cálculo do adicional e soma com o salário inicial
print('O salário final será: %d' % (xSalFinal)) #Mostra na tela o salário final
