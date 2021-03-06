

#importe as bibliotecas
import numpy as np
import sys 
import sounddevice as sd
from suaBibSignal import *
import time as ZaWarudo


def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)

def main():
    print("Inicializando encoder")
    
     #declare um objeto da classe da sua biblioteca de apoio (cedida)    
    #declare uma variavel com a frequencia de amostragem, sendo 44100
    signal= signalMeu()
    freqDeAmostragem = 44100
    
    #voce importou a bilioteca sounddevice como, por exemplo, sd. entao
    # os seguintes parametros devem ser setados:
    sd.default.samplerate = freqDeAmostragem #taxa de amostragem
    sd.default.channels = 2  #voce pode ter que alterar isso dependendo da sua placa
    
    duration = 5#tempo em segundos que ira emitir o sinal acustico 
      
#relativo ao volume. Um ganho alto pode saturar sua placa... comece com .3    
    gainX  = 0.3
    gainY  = 0.3
    
    amplitude = 1.5

    print("Gerando Tons base")
    
    #gere duas senoides para cada frequencia da tabela DTMF ! Canal x e canal y 
    #use para isso sua biblioteca (cedida)
    #obtenha o vetor tempo tb.
    digits = {
    "1":[1209,697], "2":[1336,697], "3":[1477,697], "4":[1209,770], 
    "5":[1336,770], "6":[1477,770], "7":[1209,852], "8":[1336,852],
    "9":[1477,852], "0":[1336,941]
    }
    T = duration
    fs = freqDeAmostragem
    #deixe tudo como array
    t   = np.linspace(-T/2,T/2,T*fs)
    y = t
    #printe a mensagem para o usuario teclar um numero de 0 a 9.
    digit = int(input("Escolha um número de 0 a 9:"))
    #nao aceite outro valor de entrada.
    while not 0 <= digit <=9:
        print("Entrada inválida")
        digit = int(input("Escolha um número de 0 a 9:"))

    print("Gerando Tom referente ao símbolo : {}".format(digit))
    #construa o sunal a ser reproduzido. nao se esqueca de que é a soma das senoides
    valors = digits[str(digit)]
    x1,y1 = signal.generateSin(valors[0],amplitude, duration, freqDeAmostragem)
    x2,y2 = signal.generateSin(valors[1],amplitude, duration, freqDeAmostragem)
    x = y1 + y2

    #printe o grafico no tempo do sinal a ser reproduzido

    plt.plot(y,x)
    # reproduz o som
    tone = x*gainX
    sd.play(tone, fs)
    # Exibe gráficos
    plt.show()
    # aguarda fim do audio
    sd.wait()

if __name__ == "__main__":
    main()
