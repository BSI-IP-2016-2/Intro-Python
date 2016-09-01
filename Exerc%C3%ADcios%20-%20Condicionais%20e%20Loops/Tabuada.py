'''
Created on 1 de set de 2016

@author: Netthacker
'''
#Criação da tabuada
#Definindo as variáveis:
multi=int(input('Digite o número para fazer a tabuada:'))
total= 1
print('Tabuada de %d:'%(multi))

#Criando o laço com o for
for i in range(1,11,1):
    total=multi*i
    print('%d X %d = %d'%(multi,i,total))