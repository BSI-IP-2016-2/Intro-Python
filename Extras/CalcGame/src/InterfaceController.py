import MainController

msg1 = "Bem-vindo(a) ao jogo da calculadora randômica"
msg2 = "Você deverá responder o valor correto há cada vez que uma nova conta aparecer"
msg3 = "Respostas erradas geram -1 ponto, respostas corretas adicionam 1 ponto."
msg4 = "Se você chegar a 0 pontos, você perderá o jogo."
msg5 = "Você terá 5, 10 ou 15 segundos para responder cada questão"
msg6 = "Boa sorte!!!"
msg7 = "Por favor, escolha a dificuldade e o tipo de cálculo para iniciar"
msg8 = "1 - Fácil __ 2 - Médio __ 3 - Difícil / 1 - Adição __ 2 - Subtração"

def StartGame():
    print(msg1.center(100, '█'))
    print(msg2.center(100, '█'))
    print(msg3.center(100, '█'))
    print(msg4.center(100, '█'))
    print(msg5.center(100, '█'))
    print(msg6.center(100, '█'))  
    print(msg7.center(100, '▒'))
    print(msg8.center(100, '▒'))
    
if __name__ == "__main__":
    StartGame()
    MainController.ResetValuesAtStart()