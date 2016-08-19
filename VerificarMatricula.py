# Forma em Python 2.x para exibir a matricula do aluno no python atualizado:

Nome = str(input("Digite o nome do aluno: ")) #Mostra na tela o input para o nome do aluno ser digitado
Matr = 0 #Define a variável inicial da matrícula
while True: #Entra no loop para verificar se a matrícula está sendo digitadas em números inteiros
	try:
		Matr = int(input("Digite o número da matrícula do aluno: "))
	except ValueError:
		print("O número de matrícula deve conter apenas números")
		continue #Senão for, entra no loop e pede novamente para digitar a matrícula
	else:
		break #Fecha o loop caso esteja tudo certo
print ("Nome do Aluno: " + Nome + ",", "Matricula: %s" %(Matr)) #Exibe o nome do aluno e a matrícula na formatação exigida


# Forma em Python 2.x para exibir a matricula do aluno no python atualizado:

nome = raw_input('Escreva o nome do aluno:') # Mostra na tela para digitar o nome do aluno
matricula = 0 #define a variável inicial da matrícula
while True: #setando o loop
    try:
        matricula = int(input('Escreva o numero de matricula do aluno:'))
    except ValueError:
        print('Apenas numeros na matricula')
        continue # enquanto não for numero, solicita uma numeração válida
    else:
        break # fecha o loop 
print('O nome do aluno e: '+ nome + ' e sua matricula e: %s'%(matricula)) # exibe o solicitado na tela
