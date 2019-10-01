##### SOCKET CLIENT

import sys
import socket
import time
import threading
  

print('Digite o IP do servidor')
IP = input()

print('Entre com a porta do Servidor')
Port = int(input())

print('Entre com o ID do Cliente')
ID = input()

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    sock.connect((IP,Port))
    sock.send(bytes(ID,'utf-8'))
except:
    print('### Bind Error, closing session ###')
    time.sleep(2)
    sys.exit()

print('Qual e Numero do Transformador?')
N_serie = input()
sock.send(bytes(N_serie,'utf-8'))

print('Qual e a Tensao rms esperada?')
V=input()
sock.send(bytes(V,'utf-8'))

print('Qual e o erro esperado? (em %)')
erro=input()
sock.send(bytes(erro,'utf-8'))

while True:
    n=0
    time.sleep(2)
    while True:
        print('Digite a Tensão Pico a Pico')
        tensao = input()
        sock.send(bytes(tensao,'utf-8'))
       
        
       # n=-1
        #sock.send(bytes(n,'utf-8'))
    
        
    
        
    
        
    

