import socket
import sys
import time
import errno
import math
import os
from _thread import *
from multiprocessing import Process
 
def logf(s_sock):
    while True:
        s_sock.send(str.encode('Enter a number for log 10 :'))
        num = s_sock.recv(2048)
        result = math.log10(int(num)) 
        print(result)
        s_sock.sendall(bytes(str(result),'utf8'))
        break
    s_sock.close()

def expf(s_sock):
    while True:
        s_sock.send(str.encode('Enter a number for exponential :'))
        num = s_sock.recv(2048)
        result = math.exp(int(num)) 
        print(result)
        s_sock.sendall(bytes(str(result),'utf8'))
        break
    s_sock.close()

def sqrtf(s_sock):
    while True:
        s_sock.send(str.encode('Enter a number for square root :'))
        num = s_sock.recv(2048)
        result = math.sqrt(int(num)) 
        print(result)
        s_sock.sendall(bytes(str(result),'utf8'))
        break
    s_sock.close()

def procf (s_sock):
        respond = s_sock.recv(2048).decode()
        print(respond) 
        while not (respond == "Q"):
            if respond == "L":                   
                p1 = Process(target=logf, args=(s_sock,))
                p1.start()
                p1.join()
                p1.close()
            elif respond == "E":                   
                p2 = Process(target=expf, args=(s_sock,))
                p2.start()
                p2.join()
                p2.close()
            elif respond == "S":
                p3 = Process(target=sqrtf, args=(s_sock,))
                p3.start()
                p3.join()
                p3.close()
            respond = s_sock.recv(2048).decode()
            print(respond)
        s_sock.close()
    
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888 ))
    print("listening...")
    s.listen(5)
    ThreadCount = 0
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                print('Connected to: ' + s_addr[0] + ':' + str(s_addr[1]))
                ThreadCount += 1
                print('Thread Number: ' + str(ThreadCount))
                p0 = Process(target=procf, args=(s_sock,))
                p0.start()
                p0.join()
                p0.close() 
        
            except socket.error:
                print('got a socket error')
            print('Thank you !')
    except Exception as e:        
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
     	   s.close()
