# Cálculo da Velocidade Média, usando tanto minutos quanto horas.

    print('Exercício de Velocidade Média')
dist = 0 # Defina as variáveis
temp = 0
x = 0
y = 0
while True: # abrir o loop, para evitar que se ponha letras em vez de números
    try:
        dist = float(input('Digite a distância percorrida: '))
        temp = float(input('Digite o tempo gasto em horas ou em minutos: '))
        x = int(input('Digite 1 se utilizou horas ou 2 se utilizou minutos: '))
    except ValueError:
        print('Somente números !')
        continue
    else:
        break

#Definindo se x == 1, 2 ou se nenhum dos 2

if x == 1:
    y = dist/temp
elif x == 2:
    y = dist*60/temp
else:
    print('Erro, Digite 1 para horas ou 2 para minutos!')  # Caso não selecione 1 ou 2, o cálculo vai dar 0 e vai dar Erro  

#o próximo if está relacionado se o y for maior que 110 ou não !

if y > 110 :
    print('Velocidade média acima de 110km/h, sua velocidade foi de : %s km/h'%(y))
else:
    print('Sua velocidade foi de: %s km/h'%(y))
