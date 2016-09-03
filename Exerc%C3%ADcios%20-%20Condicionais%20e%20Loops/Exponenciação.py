'''
Created on 3 de set de 2016

@author: netthacker
'''
base = int(input('Escreva a base: '))
exp = int(input('Escreva o expoente: '))
resultado = 1
i = 0
while i < exp:
    resultado*=base
    i+=1
    print(resultado)