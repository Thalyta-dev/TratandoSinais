import subprocess
import os
import signal
import time

pid=0
print("Digite o pid: ")
pid=input()

print("Mandando o signal")  


time.sleep(3)
print("Mandando o signal SiGINT")
os.kill(int(pid),signal.SIGINT)

time.sleep(3)
    
print("Mandando o signal SIGTERM")
os.kill(int(pid), signal.SIGTERM)


time.sleep(3)

print("Mandando o signal SIGKILL")
os.kill(int(pid), signal.SIGKILL)
