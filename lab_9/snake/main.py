import pygame, sys, time, random

difficulty = 10
food_timer = 50  # Initial value for food timer

# Window size
frame_size_x = 720
frame_size_y = 480

pygame.init()

# Initialise game window
pygame.display.set_caption("Snake Eater")
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]

food_pos = [
    random.randrange(1, (frame_size_x // 10)) * 10,
    random.randrange(1, (frame_size_y // 10)) * 10,
]
food_spawn = True

direction = "RIGHT"
change_to = direction

score = 0
level = 1


# Game Over
def game_over():
    my_font = pygame.font.SysFont("times new roman", 90)
    game_over_surface = my_font.render("YOU DIED", True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, "times", 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score : " + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
    game_window.blit(score_surface, score_rect)


def show_level(choice, color, font, size):
    level_font = pygame.font.SysFont(font, size)
    level_surface = level_font.render("Level : " + str(level), True, color)
    level_rect = level_surface.get_rect()
    if choice == 1:
        level_rect.midtop = (frame_size_x / 10, 40)
    else:
        level_rect.midtop = (frame_size_x / 2, frame_size_y / 2)
    game_window.blit(level_surface, level_rect)


# Main logic
while True:
    if score >= level * 5:
        level += 1
        difficulty += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord("w"):
                change_to = "UP"
            if event.key == pygame.K_DOWN or event.key == ord("s"):
                change_to = "DOWN"
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                change_to = "RIGHT"
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
        food_timer = 50  # Reset food timer
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [
            random.randrange(1, (frame_size_x // 10)) * 10,
            random.randrange(1, (frame_size_y // 10)) * 10,
        ]
        food_spawn = True

    # Decrement food timer
    food_timer -= 1
    if food_timer == 0:
        food_spawn = False

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, white, "consolas", 20)
    show_level(1, white, "consolas", 20)
    pygame.display.update()
    fps_controller.tick(difficulty)
