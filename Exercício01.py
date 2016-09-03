'''
Created on 1 de set de 2016

@author: Netthacker
'''
nome=input('Escreva seu nome: ')
endereço=input('Escreva seu endereço: ')
curso=input('Escreva seu curso: ')
idade=int(input('Digite sua idade: '))
altura=float(input('Digite sua altura: '))
peso=float(input('Digite seu peso: '))
sexo= input('M-masculino ou F-feminino: ')
if sexo.upper()=="F":
    print('%s, reside no endereço %s, é aluna do curso: %s. Ela tem %d anos, com %.2f de altura, pesando %.2f Kg '%(nome,endereço,curso,idade,altura,peso))
else:
    print('%s, reside no endereço %s, é aluno do curso: %s. Ele tem %d anos, com %.2f de altura, pesando %.2f Kg '%(nome,endereço,curso,idade,altura,peso))