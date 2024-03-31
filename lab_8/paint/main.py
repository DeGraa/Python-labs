import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = "blue"
    points = []
    drawing = False
    color = (255, 255, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = "red"
                elif event.key == pygame.K_g:
                    mode = "green"
                elif event.key == pygame.K_b:
                    mode = "blue"
                elif event.key == pygame.K_c:
                    color_picker(screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click
                    drawing = True
                    points = []
                    points.append(event.pos)
                elif event.button == 3:  # right click
                    drawing = True
                    points = []
                    points.append(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:  # left or right click
                    drawing = False
                    points = []
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    position = event.pos
                    points.append(position)

        screen.fill((0, 0, 0))

        if len(points) > 1:
            for i in range(len(points) - 1):
                pygame.draw.line(screen, color, points[i], points[i + 1], radius * 2)

        pygame.display.flip()

        clock.tick(60)


def color_picker(screen):
    color_palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255), (0, 0, 0)]
    color_buttons = []
    for i, color in enumerate(color_palette):
        button = pygame.Rect(10 + i * 50, 10, 40, 40)
        pygame.draw.rect(screen, color, button)
        color_buttons.append(button)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(color_buttons):
                    if button.collidepoint(event.pos):
                        return color_palette[i]
        pygame.display.update()


main()
