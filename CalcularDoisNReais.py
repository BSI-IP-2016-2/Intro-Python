x, y = (0,)*2
while True:
    try:
        x = float(input("Digite um número real: "))
    except ValueError:
        print("Por favor, digite apenas números inteiros")
        continue
    else:
        break
while True:
    try:
        y = float(input("Digite um segundo número real: "))
    except ValueError:
        print("Por favor, digite apenas números inteiros")
        continue
    else:
        break
print(x * y)
