import signal
import os


#Aqui estamos definindo uma função amnipuladora de eventos para tratar os sinais recebidos, o signum é o numero do sinal, e o stack é a pilha de execução do programa
def recebendoSinais(signum, frame):
    
    if signum == signal.SIGINT:
        
        print ('O Sinal recebido foi SIGINT')
        
    elif signum == signal.SIGTERM:
        
          print ('O Sinal recebido foi SIGTERM')



print ('My PID is:', os.getpid()) 

#Aqui estamos capturando os sinais
signal.signal(signal.SIGINT, recebendoSinais)
signal.signal(signal.SIGTERM, recebendoSinais)

#Enquanto o programa estiver em execução vamos continuar recebendo os sinais
while True:   
    print("AGUARDANDO O SINAL...")     
    
    #Aqui, só receberemos os sinais depois que o anterior for tratado
    signal.pause()

