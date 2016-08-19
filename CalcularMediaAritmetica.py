x, y, z = (0,)*3 #Define as variáveis necessárias que iremos precisar
while True:
    try: #Faz a verificação da primeira nota
        x = float(input("Digite a primeira nota: "))
    except ValueError:
        print("Por favor, digite apenas números")
        continue
    else:
        break #Fecha o loop se estiver tudo certo
while True: #Faz a verificação da segunda nota
    try:
        y = float(input("Digite a segunda nota: "))
    except ValueError:
        print("Por favor, digite apenas números")
        continue
    else:
        break #Fecha o loop se estiver tudo certo
while True: #Faz a verificação da terceira nota
    try:
        z = float(input("Digite a terceira nota: "))
    except ValueError:
        print("Por favor, digite apenas números")
        continue
    else:
        break #Fecha o loop se estiver tudo certo
print((x + y + z) / 3) #Faz o cálculo final e mostra na tela
