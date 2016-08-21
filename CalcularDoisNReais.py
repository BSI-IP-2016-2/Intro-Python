x, y = (0,)*2 #Define as duas variáveis iniciais que serão usadas
while True:
    try:
        x = float(input("Digite um número real: ")) #Verifica se o número digitado é um float (inteiro ou decimal)
    except ValueError:
        print("Por favor, digite apenas números reais") #Joga a mensagem de erro pro usuário saber o que ocorreu e digitar de novo
        continue
    else:
        break #Fecha o loop
while True: #Abre um novo loop para esperar o segundo número
    try:
        y = float(input("Digite um segundo número real: "))
    except ValueError:
        print("Por favor, digite apenas números reais")
        continue
    else:
        break
print(x * y) #Faz o cálculo final e mostra pro usuário
