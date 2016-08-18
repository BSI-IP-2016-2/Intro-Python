def calcRet():
    x = input("Digite a base: ")
    while not x:
        x = input("Digite a base: ")
    y = input("Digite a altura: ")
    while not y:
        y = input("Digite a altura: ")
    if int(x) == 0 or int(y) == 0:
        print("O valor digitado está incorreto. Por favor, tente novamente: ")
        return calcRet()
    elif int(x) > 0 and int(y) > 0:
        print(int(x) * int(y))
        return ()

if __name__ == '__main__':
    calcRet()
