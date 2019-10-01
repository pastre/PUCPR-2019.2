########## SOCKET SERVER

import socket
import sys
import time
import math
import threading 
import requests


ip, porta = input("Entre com o IP da API"), int(input("Entre com a porta da API"))

API_URL = f"http://{ip}:{porta}/vpp"

        
class Trafo:
    def __init__(self, tId, serie, tensaoRef, error):
        self.tId = tId
        self.serie = serie
        self.tensaoRef = tensaoRef
        self.error = error
        self.tensions = []

    def add_voltage(self, t):
        self.tensions.append(t)

    def media(self):
        return sum(self.tensions) / len(self.tensions)

    def is_approved(self, t):
        error = (self.tensaoRef - t) / (self.tensaoRef)
        return [error, "aprovado"] if error < (self.error / 100) else [error, "reprovado"]

    def get_list(self, Vpp):
        error, status = self.is_approved(Vpp)
        media = self.media()

        return {
            "tId" : self.tId ,
            "serie" : self.serie ,
            "tensaoRef" : self.tensaoRef ,
            "errorRef" : self.error ,
            "error": error,
            "status": status,
            "media": media
        }



def write(vpp):
    try:
        requests.post(API_URL, vpp)
    except Exception as e:
        print("deu ruim pra enviar pro sv", e)


def RecebeDado(conn,addr):
    print('A thread', addr, 'iniciou')
    ID = str(conn.recv(10),'utf-8')
    print('O Transformador ', ID, ' registrado no socket')
    
    Nserie = int(conn.recv(10))
    VoltageRMS = float(conn.recv(10))
    Erro = float(conn.recv(10))

    print('---', ID, Nserie, VoltageRMS, Erro)
    n=0

    t1 = Trafo(ID,Nserie,VoltageRMS,Erro)

    while n != -1:
        Vpp = int(conn.recv(10))
        print('Recebi')
        t1.add_voltage(Vpp)

        if Vpp == int(0) :
            print('Encerrei')
            break
        else:
            wr = t1.get_list(Vpp)
            print("Sending", wr, "to the server")
            write(wr)
            



print('Digite um Numero de Porta')
Port = int(input())

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET = IPv4 SOCK_STREAM = TCP

try:
    sock.bind(('0.0.0.0',Port))
except:
    print('### Bind Error, closing session ###')
    time.sleep(2)
    sys.exit()

sock.listen(2)
print('Aguardando conexoes em: ',Port)

while True :
    conn, addr = sock.accept()
    print('Conexao estabelecida com: ',addr)
    t = threading.Thread(target=RecebeDado,args=(conn,addr))
    t.start()
    
print('A Sessao com: ',addr,' foi encerrada')
sock.close()
