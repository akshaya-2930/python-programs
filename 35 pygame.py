import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Ball settings
ball_pos = [100, 100]
ball_radius = 20
ball_speed = [4, 4]

# Clock for frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce off the walls
    if ball_pos[0] <= ball_radius or ball_pos[0] >= width - ball_radius:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= ball_radius or ball_pos[1] >= height - ball_radius:
        ball_speed[1] = -ball_speed[1]

    # Draw everything
    window.fill(white)
    pygame.draw.circle(window, red, ball_pos, ball_radius)
    pygame.display.flip()
    clock.tick(60)
