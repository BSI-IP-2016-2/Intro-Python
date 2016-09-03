'''
Created on 3 de set de 2016

@author: netthacker
'''
#Criação de um menu explicativo:

print('Pesquisa de perfil de aluno: ')
print('1 - Primeira série')
print('2 - Segunda série')
print('3 - Terceira série')
print('4 - Quarta série')
print('Sim - Gosta de redação')
print('Não - Não gosta de redação')
print('Digite 0 para sair')

#Definição das variáveis:
serie = 0 
primeira = 0
segunda = 0
terceira = 0
quarta = 0
gostaredacao = ''
livroslidos = 0
maislivroslidos = 0
naofazred=0
maisde1livro = 0
gostared = 0
gostaredelerlivro=0

#Laço maior:
while True:
    #Laço de checagem, testando os valores para ver se são válidos
    while True:    
        try:
            serie = int(input('Digite sua série: '))
            break
        except:
            print('Valores inválidos, coloque-os novamente !')
    
    #ponto de parada para sair do laço principal.
    if serie == 0:
        break
    while True:
        try:
            livroslidos = int(input('Digite quantos livros leu: '))
        except:
            print('Valores inválidos, coloque-os novamente !')
    while True:
        try:
            gostaredacao = str(input('Você gosta de redação: '))
        except:
            print('Valores inválidos, coloque-os novamente !')        
    
    #Fazendo o gosta de redação como true or false
    if gostaredacao.upper() == 'Sim':
        gostaredacao = True
    else:
        gostaredacao = False
    
    #Código de construção da solução do problema propriamente dito
    if serie == 1:
        primeira+=1
        if livroslidos > 1 and gostaredacao == True:
            #Não é preciso dessas duas variáveis, só pus aqui como forma de contagem
            maisde1livro +=1
            gostared +=1
            #solução do problema 
            gostaredelerlivro +=1    
    elif serie == 2:
        segunda +=1
        if gostaredacao == False:
            naofazred+=1
    elif serie == 3:
        terceira+=1
    elif serie ==4:
        quarta +=1
        if livroslidos > maislivroslidos:
            maislivroslidos = livroslidos
    
    

print('Temos %d alunos da Terceira série.'%(terceira))
print('A maior quantidade de livros lidos por um aluno da Quarta série é : %d'%(maislivroslidos))
#É necessário criar esse ponto de checagem, pois caso não crie e não tiver alunos da 2º série, vai dar erro no sistema
if segunda > 0:
    print('A porcentagem de alunos da segunda série que não gosta de fazer redação é de %.2f%%'%(naofazred*100/segunda))

print('Não há alunos da segunda série')
print('Tem %d alunos da primeira série que gostam de ler livro e de redação'%(gostaredelerlivro))
print('Temos %d alunos'%(primeira+segunda+terceira+quarta))