x, y, z = (0,)*3
while True:
    try:
        x = float(input("Digite a primeira nota: "))
    except ValueError:
        print("Por favor, digite apenas números")
        continue
    else:
        break
while True:
    try:
        y = float(input("Digite a segunda nota: "))
    except ValueError:
        print("Por favor, digite apenas números")
        continue
    else:
        break
while True:
    try:
        z = float(input("Digite a terceira nota: "))
    except ValueError:
        print("Por favor, digite apenas números")
        continue
    else:
        break
print((x + y + z) / 3)
