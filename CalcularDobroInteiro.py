x = 0
while True:
    try:
        x = float(input("Digite um número inteiro: "))
    except ValueError:
        print("Por favor, digite apenas números inteiros")
        continue
    else:
        break
print(x * 2)
