'''
Created on 21 de ago de 2016

@author: NettHacker
'''

if __name__ == '__main__':
    print('Fatorial de um número')
    fat = int(input('Digite um número: '))
    i = fat
while i>1:
    i = i-1
    fat = fat*i
    continue
else:
    print('O resultado do fatorial é: %s'%(fat))