'''
Created on 2 de set de 2016

@author: Netthacker
'''
dia = int(input('Digite o dia que você nasceu: '))
mes = int(input('Digite o mês que você nasceu: '))
ano = int(input('Digite o ano que você nasceu: '))
diaatual = int(input('Digite o dia atual: '))
mesatual = int(input('Digite o mês atual: '))
anoatual = int(input('Digite o ano atual: '))
a = dia #cálculo para saber quantos dias faltam para o ano acabar
b = (mes*30) #cálculo para saber quantos meses faltam para o ano acabar
c = (ano*365) #cálculo para saber quantos dias do ano faltam para o ano acabar

d = diaatual
e = (mesatual*30) #cálculo para saber quantos meses do ano atual faltam para o ano acabar
f = (anoatual*365) #cálculo para saber quantos dias do ano atual faltam para o ano acabar


g = d+e+f -(a+b+c)
print(g)