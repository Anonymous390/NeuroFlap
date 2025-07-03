from flappy import FlappyBirdEnv
import pygame
import numpy as np

WIDTH, HEIGHT = 400, 600
BIRD_RADIUS = 15
PIPE_WIDTH = 60
GAP_HEIGHT = 150
GRAVITY = 0.5
JUMP_STRENGTH = -8
FPS = 30

WHITE = (255, 255, 255)

env = FlappyBirdEnv(render=True)
state = env.reset()

pygame.font.init()
font = pygame.font.SysFont('Arial', 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not env.done:
        action = 1 if keys[pygame.K_SPACE] else 0
        state, reward, done = env.step(action)
        env.render()
        pygame.display.flip()

    else:
        env.draw_game_over()

        if keys[pygame.K_r]:
            state = env.reset()
        if keys[pygame.K_ESCAPE]:
            running = False

pygame.quit()
