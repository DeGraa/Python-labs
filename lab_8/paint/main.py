import pygame

# Initialize Pygame
pygame.init()

# Constants for the application
FPS = 120
WIDTH, HEIGHT = 800, 600
MENU_HEIGHT = 70
BRUSH_SIZE = 20
RECT_WIDTH, RECT_HEIGHT = 37, 20

# Initialize the screen and timer
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
timer = pygame.time.Clock()

# Variables for the painting app
active_figure = 0  # 0 for circle, 1 for rectangle
active_color = "white"
painting = []  # List to hold all the painting actions


def draw_menu(active_color):
    """
    Draws the menu with brush options and colors.
    """
    # Menu background
    pygame.draw.rect(screen, "gray", (0, 0, WIDTH, MENU_HEIGHT))
    pygame.draw.line(screen, "black", (0, MENU_HEIGHT), (WIDTH, MENU_HEIGHT), 3)

    # Brush options
    circle_brush_rect = pygame.draw.rect(screen, "black", (10, 10, 50, 50))
    pygame.draw.circle(screen, "white", (35, 35), BRUSH_SIZE)
    pygame.draw.circle(screen, "black", (35, 35), BRUSH_SIZE - 2)

    rect_brush_rect = pygame.draw.rect(screen, "black", (70, 10, 50, 50))
    pygame.draw.rect(screen, "white", (76.5, 26, RECT_WIDTH, RECT_HEIGHT), 2)

    brush_list = [(circle_brush_rect, 0), (rect_brush_rect, 1)]

    # Active color indicator
    pygame.draw.circle(screen, active_color, (400, 35), 30)
    pygame.draw.circle(screen, "dark gray", (400, 35), 30, 3)

    # Color options
    color_positions = [
        (WIDTH - 35, 10),
        (WIDTH - 35, 35),
        (WIDTH - 60, 10),
        (WIDTH - 60, 35),
        (WIDTH - 85, 10),
        (WIDTH - 85, 35),
        (WIDTH - 110, 10),
    ]
    colors = [
        (0, 0, 255),
        (255, 0, 0),
        (0, 255, 0),
        (255, 255, 0),
        (0, 255, 255),
        (255, 0, 255),
        (0, 0, 0),
    ]
    color_rects = [
        pygame.draw.rect(screen, color, (pos[0], pos[1], 25, 25))
        for pos, color in zip(color_positions, colors)
    ]
    color_rects.append(
        pygame.draw.rect(screen, "black", (WIDTH - 150, 10, 25, 25))
    )  # Eraser

    return (
        brush_list,
        color_rects,
        colors + [(255, 255, 255)],
    )  # Adding white for the eraser


def draw_painting(paints):
    """
    Draws the painting actions stored in the paints list.
    """
    for color, pos, figure in paints:
        if color == (255, 255, 255):  # Eraser
            pygame.draw.rect(
                screen, color, (pos[0] - 15, pos[1] - 15, RECT_WIDTH, RECT_HEIGHT)
            )
        else:
            if figure == 0:  # Circle brush
                pygame.draw.circle(screen, color, pos, BRUSH_SIZE)
            elif figure == 1:  # Rectangle brush
                pygame.draw.rect(
                    screen, color, (pos[0] - 15, pos[1] - 15, RECT_WIDTH, RECT_HEIGHT)
                )


def main():
    run = True
    global active_color, active_figure

    while run:
        timer.tick(FPS)
        screen.fill("white")
        mouse = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]

        brushes, colors, rgbs = draw_menu(active_color)

        if left_click and mouse[1] > MENU_HEIGHT:
            painting.append((active_color, mouse, active_figure))

        draw_painting(painting)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, color_rect in enumerate(colors):
                    if color_rect.collidepoint(event.pos):
                        active_color = rgbs[i]
                for brush_rect, figure in brushes:
                    if brush_rect.collidepoint(event.pos):
                        active_figure = figure

        pygame.display.flip()

    pygame.quit()


main()
