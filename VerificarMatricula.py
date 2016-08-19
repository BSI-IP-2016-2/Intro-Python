Nome = str(input("Digite o nome do aluno: "))
Matr = 0
while True:
	try:
		Matr = int(input("Digite o número da matrícula do aluno: "))
	except ValueError:
		print("O número de matrícula deve conter apenas números")
		continue
	else:
		break
print ("Nome do Aluno: " + Nome + ",", "Matricula: %s" %(Matr))
