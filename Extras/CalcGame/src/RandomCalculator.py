import random
import MainController

x, y = (0,)*2;
rDif = 0;
CalcType = 0;

def ReceiveDataFromMain(mDif, cType):
    global rDif
    global CalcType
    rDif = mDif
    CalcType = cType
    RandomGeneratorN1()

def RandomGeneratorN1():
    
    if (rDif == 1):
        x = random.randrange(0, 10);
        y = random.randrange(5, 15);
    elif (rDif == 2):
        x = random.randrange(5, 25);
        y = random.randrange(8, 19);
    else:
        x = random.randrange(0, 35);
        y = random.randrange(3, 25);
        
    GenerateAnswer(x, y)
    
def GenerateAnswer(x, y):
 
    if(CalcType == 1):   
        print(x, "+", y)
        xy = x + y
    elif(CalcType == 2):
        print(x, "-", y)
        xy = x - y
    
    inputAnswer = input("Qual é resposta: ")
    
    if (inputAnswer == "sair"  or inputAnswer == "exit"):
        MainController.ResetValuesAtStart()
    else:
        CheckAnswer(inputAnswer, xy)
        
def CheckAnswer(answer, xy):
    
    if(int(answer) == xy):
        print("Acertou")
        RandomGeneratorN1()
    else:
        print("Errou")
        RandomGeneratorN1()