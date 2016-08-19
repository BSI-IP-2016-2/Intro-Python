x, y = (0,)*2
while True:
    try:
        x = int(input("Digite a base: "))
    except ValueError:
        print("Você não pode deixar o espaço vazio ou digitou uma letra")
        continue
    else:
        break
while True:
    try:
        y = int(input("Digite a altura: "))
    except ValueError:
        print("Você não pode deixar o espaço vazio ou digitou uma letra")
        continue
    else:
        break
if x > 0 and y > 0:
    print(x * y)
