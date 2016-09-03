'''
Created on 1 de set de 2016

@author: Netthacker
'''

print('Digite 10 números e veja se são pares ou ímpares')
#Definindo as variáveis
par = 0
impar = 0
totalpar = 0
totalimpar = 0
qntImpar = 0
qntpar = 0

for i in range(10): #Definindo um range, no caso são 10 números
    a = float(input('Digite o número: ')) #Definindo uma variável no caso o a, deixei float para a média dos ímpares
    if a%2 == 0: #Determinando um número par
        par = a 
        qntpar += 1 #Quantidade de numero par, para a contagem 
        totalpar += par #total de números pares, somando ele ao número par encontrado
    elif a%2 != 0: #Definição de um número ímpar, vide if acima
        impar = a
        qntImpar += 1
        totalimpar += impar
        print('O total de números pares são: %d'%(qntpar))
        print('O total de números impares são: %d'%(qntImpar))
        print('A soma dos pares são: %d'%(totalpar))
        print('A média dos ímpares são: %f'%(totalimpar/qntImpar))
    elif qntImpar == 0: #Para o caso de não existir impar, pois não dá pra se dividir por 0.
        print('O total de números pares são: %d'%(qntpar))
        print('O total de números impares são: %d'%(qntImpar))
        print('A soma dos pares são: %d'%(totalpar))
        print('A média dos ímpares é 0')


