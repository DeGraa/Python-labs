import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

button_size = 60
play_button = pygame.transform.scale(
    pygame.image.load(os.path.normpath("lab_7/music_player/img/play.png")),
    (button_size, button_size),
)
pause_button = pygame.transform.scale(
    pygame.image.load(os.path.normpath("lab_7/music_player/img/pause.png")),
    (button_size, button_size),
)

songs = [
    "lab_7/music_player/music/reflections.mp3",
    "lab_7/music_player/music/popular.mp3",
    "lab_7/music_player/music/from-the-start.mp3",
]

covers = [
    "lab_7/music_player/img/reflections.jpeg",
    "lab_7/music_player/img/popular.jpg",
    "lab_7/music_player/img/fromthestart.jpg",
]

current_song_index = 0
pygame.mixer.music.load(os.path.normpath(songs[current_song_index]))
pygame.mixer.music.play()

album_cover_size = 275
album_cover = pygame.transform.scale(
    pygame.image.load(os.path.normpath(covers[current_song_index])),
    (album_cover_size, album_cover_size),
)

play = True
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        play = not play
        if play:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

    if pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
        if pressed[pygame.K_LEFT]:
            current_song_index = (current_song_index - 1) % len(songs)
        else:
            current_song_index = (current_song_index + 1) % len(songs)

        pygame.mixer.music.load(songs[current_song_index])
        pygame.mixer.music.play()
        play = True
        album_cover = pygame.transform.scale(
            pygame.image.load(covers[current_song_index]),
            (album_cover_size, album_cover_size),
        )

    screen.fill((255, 255, 255))
    screen.blit(album_cover, (270, 65))

    if play:
        screen.blit(pause_button, (380, 365))
    else:
        screen.blit(play_button, (380, 365))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
