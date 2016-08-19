##### Semelhante ao código normal, porém usa uma função para chamar os códigos #####
##### Os comentários restantes estão no outro código ###############################

def calcRet(): #Define uma função (pode ser qualquer nome)
    x, y = (0,)*2
    while True:
        try:
            x = int(input("Digite a base: "))
        except ValueError:
            print("Você não pode deixar o espaço vazio ou digitou uma letra")
            continue
        else:
            break
    while True:
        try:
            y = int(input("Digite a altura: "))
        except ValueError:
            print("Você não pode deixar o espaço vazio ou digitou uma letra")
            continue
        else:
            break
    if x > 0 and y > 0:
        print(x * y)
        return () #Se certifica que essa função foi finalizada

if __name__ == '__main__': #Chama a função (sem essa parte, a função não entra e o código nunca inicia)
    calcRet()

