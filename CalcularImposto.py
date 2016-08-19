xCheque = 0
while True:
    try:
        xCheque = float(input("Digite o salário: "))
    except ValueError:
        print("Você não pode deixar o espaço vazio ou digitou uma letra")
        continue
    else:
        break
Tax = xCheque * 0.3
print('O salário final será: %d' % (Tax))