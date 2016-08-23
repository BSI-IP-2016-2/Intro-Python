# Main Controller Script
# This script controls the main part of the game. Including menus

import RandomCalculator

dif = 0;
cType = 0;

def ResetValuesAtStart():
    global dif
    global cType
    dif = 0
    cType = 0
    ChooseDif()

def ChooseDif():
    
    difList = [1, 2, 3];
    cTypeList = [1, 2];

    while True:
        try:
            dif = int(input("Escolha a sua dificuldade: "))
            cType = int(input("Escolha o tipo de conta: "))
            if (dif not in difList or cType not in cTypeList):
                raise ValueError
        except ValueError:
            print("Você não escolheu nenhuma dificuldade válida, por favor, escolha uma dificuldade: ")
            continue
        else:
            RandomCalculator.ReceiveDataFromMain(dif, cType)
            break

if __name__ == "__main__":
    ChooseDif()