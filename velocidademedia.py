'''
Created on 19 de ago de 2016

@author: NettHacker
'''

if __name__ == '__main__':
    print('Exercicio da velocidade media')
vel1 = 0
vel2 = 0
temp = 0
while True:
    try:
        dist = float(input('Digite a distancia percorrida: '))
        x = float(input('Se o tempo for em horas digite 1 se em minutos 2: '))
        temp = float(input('Se usar horas digite o tempo em horas, se minutos em minutos: '))
    except ValueError:
            print('Somente numeros, por favor!')
            continue
    else:
        break

if x == 1 :
    vel1 = dist/temp
else:
    vel2 = dist*60/temp

if vel1 > 110 or vel2 > 0 :
    print('Sua velocidade media sera acima de 110km/h, que sera de: %dkm/h'%(vel1 or vel2))
else:
    print('Sua velocidade media sera de: %s'%(vel1 or vel2))
