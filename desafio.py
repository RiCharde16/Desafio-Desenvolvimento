"""
    1) Observe o trecho de código abaixo:

    int INDICE = 13, SOMA = 0, K = 0;

    enquanto K < INDICE faça

    {

    K = K + 1;

    SOMA = SOMA + K;

    }

    imprimir(SOMA);



    Ao final do processamento, qual será o valor da variável SOMA?

    RESPOSTA: 91

"""

"""
    2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
    escreva um programa na linguagem que desejar onde, informado um número,
    ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

    IMPORTANTE:

    Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

    Codigo abaixo
"""

print(" ---- Sequencia de Fibonacci --- " .upper())

n = int(input('Insira um numero para verificar se ele esta na sequencia de fibonacci: '))

u_1 = 1
u_2 = 1
count = 0
exist = False
for vic in range(n):
    count = u_1 + u_2
    u_1 = count
    u_2 = (count - u_2)
    
    if (n == count): 
        exist = True
    
if (exist):
    print(f"\n O numero {n} existe na sequencia de fibonacci \n")
else:
    print(f"\n O numero {n} NÂO existe na sequencia de fibonacci \n")



"""
    3) Descubra a lógica e complete o próximo elemento:



    a) 1, 3, 5, 7, ___

    b) 2, 4, 8, 16, 32, 64, ____

    c) 0, 1, 4, 9, 16, 25, 36, ____

    d) 4, 16, 36, 64, ____

    e) 1, 1, 2, 3, 5, 8, ____

    f) 2,10, 12, 16, 17, 18, 19, ____

    RESPOSTAS: 

    a) 9
    b) 128
    c) 49
    d) 100
    e) 13
    f) 200
"""

"""
    4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

    Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

    RESPOSTA

    Temos que obrigatoriamente verificar 2 lampadas assim, deixando um interruptor ligado por alguns minutos para gerar calor que chamaresmo de I1,
    em seguida desligar a lampada I1 e ligar outra que sera I2 e visitar duas lampadas;

    ao visitar a sala 1 de uma das lampadas, se a lampada estiver ligada I2 = 1;

    se estiver quente I1 = 1;

    se estiver fria I3 = 1;

    repetimos o mesmo processo na outra sala e assim teremos a resposta da ultima lampada por exclusão.
"""

"""
    5) Escreva um programa que inverta os caracteres de um string.


    IMPORTANTE:

    a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

    b) Evite usar funções prontas, como, por exemplo, reverse;
"""

text = input("Digite algum texto para ser invertido: ")

newTxt = ""

for x in range(len(text)-1,-1,-1):
    newTxt += text[x]

print(f"Texto Original: {text} \n")
print(f"Texto Invertido: {newTxt} \n")
print()

    
