import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
color = (255, 255, 0)
speed = 3
x = 0
y = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed
    else:
        x = 250
        y = 250

    if 400 < x < 500 or 0 < x < 100:
        color = (255, 0, 0)
        speed = 1
    elif 0 < y < 100 or 400 < y < 500:
        color = (255, 0, 0)
        speed = 1
    else:
        speed = 3
        color = (255, 255, 0)

    if x > 500:
        x = 0
    if x < 0:
        x = 500
    if y > 500:
        y = 0
    if y < 0:
        y = 500



    win.fill((255, 255, 255))

    pygame.draw.circle(win, (color), (x, y), 50)

    pygame.display.update()

    pygame.time.delay(10)
