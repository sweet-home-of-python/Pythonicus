import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
while True:
    d = input()
    sock.send(d.encode())
    data = sock.recv(1024).decode()



sock.close()

print (data)

