x, y = (0,)*2
while True:
    try:
        x = int(input("Digite a largura: "))
    except ValueError:
        print("Você não pode deixar o espaço vazio ou digitou uma letra")
        continue
    else:
        break
while True:
    try:
        y = int(input("Digite o comprimento: "))
    except ValueError:
        print("Você não pode deixar o espaço vazio ou digitou uma letra")
        continue
    else:
        break
xy = x * y
if int(x) > 0 and int(y) > 0:
    print('A área do seu terreno é: %d' % (xy))
