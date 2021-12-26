import socket

ClientSocket = socket.socket()
host = '192.168.56.108'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

while True:
    Input = input('Insert L,E,S for Log,Modulus,Sqrt and Q to quit : ')
    ClientSocket.send(str.encode(Input))
    if Input=="Q" or Input=="q" or Input=="QUIT" or Input=="quit":
        print ("thank you")
        break
    elif Input == "L" or Input == "E" or Input == "S":        
        Response = ClientSocket.recv(1024)
        Input = input(Response.decode('utf-8'))
        ClientSocket.sendall(str.encode(Input))
    
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
    else:
        print('Wrong input !')

ClientSocket.close()
