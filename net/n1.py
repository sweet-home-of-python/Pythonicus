import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',8888))

while True:
    result = sock.recv(1024)
    print(result.decode())
    
        
sock.close()
