'''
Created on 21 de ago de 2016

@author: NettHacker
'''

if __name__ == '__main__':
    x = 99
while x>0:
    x = x-1
    if x%2 == 0:
        continue
    print(x)
else:
    print('Fim do teste')
    