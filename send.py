import os
import signal
import time

pid=0
print("Digite o pid: ")

#Vamos aguardar o usuario digitar, o pib so outro programa
pid=input()

print("Mandando o signal")  

#Vamos mandar os sinais para o outro programa, só que primeiro aguardaremos 3 segundos para que possamos ver a "magica" acontecer
time.sleep(3)
print("Mandando o signal SiGINT")

#Aqui vai ser a mesmo coisa de escrevermos no terminal
os.kill(int(pid),signal.SIGINT)

time.sleep(3)
    
print("Mandando o signal SIGTERM")
#Aqui vai ser a mesmo coisa de escrevermos no terminal
os.kill(int(pid), signal.SIGTERM)


time.sleep(3)

print("Mandando o signal SIGKILL")
#Aqui vai ser a mesmo coisa de escrevermos no terminal
os.kill(int(pid), signal.SIGKILL)
