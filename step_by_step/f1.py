import pygame
 
FPS = 60
W = 700  # ширина экрана
H = 300  # высота экрана
WHITE = (255, 255, 255)
black = (0, 0, 0)
 
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
# координаты и радиус круга
x = W // 2
y = H // 2
r = 50
 
while 1:
    sc.fill(WHITE)
 
    pygame.draw.circle(sc, black, (x, y), r)
 
    pygame.display.update()
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 3
            elif i.key == pygame.K_RIGHT:
                x += 3
            elif i.key == pygame.K_UP:
                y -= 3
            elif i.key == pygame.K_DOWN:
                y += 3
    clock.tick(FPS)