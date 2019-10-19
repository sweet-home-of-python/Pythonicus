import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    i = input().encode()
    sock.sendto(i,('127.0.0.1',8888))
    
