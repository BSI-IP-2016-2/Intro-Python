xSal = 0
while True:
    try:
        xSal = float(input("Digite o salário: "))
    except ValueError:
        print("Você não pode deixar o espaço vazio ou digitou uma letra")
        continue
    else:
        break
xSalAdicional = (xSal * 0.2) + xSal
print('O salário final será: %d' % (xSalAdicional))
