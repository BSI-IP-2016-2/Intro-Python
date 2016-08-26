'''
Created on 26/08/2016

@author: NettHacker
'''

if __name__ == '__main__':
    print('Ano Bissexto')

ano = int(input('Digite o ano a ser requisitado como bissexto: '))
if ano%4 == 0 and ano%400 == 0 and not ano%100 == 0:
    print(' é ano bissexto')
else:
    print('Não É ano bissexto')
        