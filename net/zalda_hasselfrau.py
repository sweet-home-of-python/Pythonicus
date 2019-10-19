import socket
import pygame

pygame.init()
black = (0,0,0)
sc = pygame.display.set_mode((600, 480))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.118', 8888))
sock.listen(0) 
client, addr = sock.accept() 
x,y,x2,y2 = 100,100,100,100

Play = True
while Play:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==QUIT:
            Play = False
        if keys[pygame.K_d]:
            x2+=10
        if keys[pygame.K_a]:
            x2-=10
        if keys[pygame.K_w]:
            y2-=10
        if keys[pygame.K_s]:
            y2+=10
             
    result = client.recv(1024)
    cr = result.decode()
    if cr =='right':
        x+=10
    if cr =='left':
        x-=10
    if cr =='up':
        y-=10
    if cr =='down':
        y+=10   
    sc.fill((255,255,255))
    pygame.draw.rect(sc, black, (x,y,20,20))
    pygame.draw.rect(sc, black, (x2,y2,20,20))
    pygame.time.delay(10)
    pygame.display.update()
   
   
    

