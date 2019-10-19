import socket
import pygame
pygame.init()
sc = pygame.display.set_mode((1, 1))
i = ''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.118', 8888))
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_d]:
            i = 'right'
        elif keys[pygame.K_a]:
            i = 'left'
        elif keys[pygame.K_w]:
            i = 'up'
        elif keys[pygame.K_s]:
            i = 'down'
        else:
            i = 'sos'
    mail = i.encode()
    sock.send(mail)
    i = ''
    
