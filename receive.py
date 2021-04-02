import signal
import os
import time

def receive_signal(signum, stack):
    
    if signum == signal.SIGINT:
        
        print ('O Sinal recebido foi SIGINT')
        
    elif signum == signal.SIGTERM:
        
          print ('O Sinal recebido foi SIGTERM')



print ('My PID is:', os.getpid()) 

signal.signal(signal.SIGINT, receive_signal)
signal.signal(signal.SIGTERM, receive_signal)

while True:   
    print("AGUARDANDO O SINAL...")     
    time.sleep(3)

