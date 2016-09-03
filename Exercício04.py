'''
Created on 3 de set de 2016

@author: netthacker
'''
while True:
    try:
        
        horainicio = int(input('Hora de ínicio do jogo: '))
        minutoinicio = int(input('Digite os minutos de início do jogo: '))
        horafim = int(input('Digite a hora de término do jogo: '))
        minutofim = int(input('Digite os minutos de término do jogo: '))
        break
    except:
        print('Somente números, comece digitando novamente !')
#Transformando o tempo inicial em minutos
horainiciomin = horainicio*60 
tempoiniciototal = horainiciomin + minutoinicio
#Transformando o tempo final em minutos
horafimmin = horafim*60
tempofimtotal = horafimmin + minutofim 

if tempofimtotal < tempoiniciototal:
    tempofimtotal +=1440

total = tempofimtotal - tempoiniciototal

horatotal = total // 60
mintotal =  total%60

print('O horário total foi de: %d:%.f'%(horatotal,mintotal))