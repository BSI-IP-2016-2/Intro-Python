x = 0 #Define a variável x inicial
while True: #Entra no loop
    try: 
        x = int(input("Digite um número inteiro: ")) #Verificar se o número digitado é um int(inteiro)
    except ValueError: #Senão for, joga um erro e uma mensagem pro usuário
        print("Por favor, digite apenas números inteiros")
        continue
    else:
        break #Fecha o loop quando recebe a confirmação que o número foi digitado
print(x * 2) #Cálcula o resultado
