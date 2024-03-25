import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Cirlce")
screen.fill("white")

x = 400
y = 400
speed = 20

circle_position = (x, y)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        elif event.type == pygame.QUIT:
            done = True

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_UP] and y > 25:
        y -= speed
    if pressed_keys[pygame.K_DOWN] and y < 775:
        y += speed
    if pressed_keys[pygame.K_LEFT] and x > 25:
        x -= speed
    if pressed_keys[pygame.K_RIGHT] and x < 775:
        x += speed

    circle_position = (x, y)
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, "red", circle_position, 25)
    pygame.display.update()
    clock.tick(60)
