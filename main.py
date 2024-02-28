import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-bit Adventure Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player
player_img = pygame.image.load("player.png")
player_x, player_y = 50, 50
player_speed = 5

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(player_img, (player_x, player_y))
    pygame.display.update()

def move_player(keys_pressed):
    global player_x, player_y

    if keys_pressed[pygame.K_LEFT]:
        player_x -= player_speed
    if keys_pressed[pygame.K_RIGHT]:
        player_x += player_speed
    if keys_pressed[pygame.K_UP]:
        player_y -= player_speed
    if keys_pressed[pygame.K_DOWN]:
        player_y += player_speed

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        move_player(keys_pressed)
        draw_window()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
