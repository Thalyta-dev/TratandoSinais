import os
import signal
import time

pid=input("Digite o pid: ")


#Vou usar essa função pra mandar os inais para o receive
def mandandoSinais(sinal):
    
    #Aqui vou colocar um delay para podermos ver a magica acontecer
    time.sleep(3)    
        
    #Aqui estou realmente mandando os sinais, a biblioteca os me permite mandar sinais para outro programa
    os.kill(int(pid),sinal)



print("Mandando o signal")  

print("Mandando o signal SIGINT")
mandandoSinais(signal.SIGINT)

print("Mandando o signal SIGTERM")
mandandoSinais(signal.SIGTERM)

print("Mandando o signal SIGKILL")
mandandoSinais(signal.SIGKILL)
