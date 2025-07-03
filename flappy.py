import pygame
import random
import sys

pygame.init()

# Game settings
WIDTH, HEIGHT = 400, 600
BIRD_RADIUS = 15
PIPE_WIDTH = 60
GAP_HEIGHT = 150
GRAVITY = 0.5
JUMP_STRENGTH = -8
FPS = 30

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (100, 100, 255)

class FlappyBirdEnv:
    def __init__(self, render=False):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) if render else None
        self.clock = pygame.time.Clock()
        self.render_mode = render
        self.reset()

    def reset(self):
        self.bird_y = HEIGHT // 2
        self.bird_vel = 0
        self.score = 0
        self.pipe_x = WIDTH
        self.pipe_gap_y = random.randint(100, HEIGHT - 200)
        self.done = False
        return self.get_state()

    def get_state(self):
        return [
            self.bird_y / HEIGHT,
            self.bird_vel / 10,
            (self.pipe_x - 50) / WIDTH,
            self.pipe_gap_y / HEIGHT
        ]

    def step(self, action):
        if self.done:
            return self.get_state(), 0, True

        # 1 = flap
        if action == 1:
            self.bird_vel = JUMP_STRENGTH
        self.bird_vel += GRAVITY
        self.bird_y += self.bird_vel

        self.pipe_x -= 5
        if self.pipe_x + PIPE_WIDTH < 0:
            self.pipe_x = WIDTH
            self.pipe_gap_y = random.randint(100, HEIGHT - 200)
            self.score += 1

        # Collision detection
        if self.bird_y < 0 or self.bird_y > HEIGHT:
            self.done = True
        if self.pipe_x < 50 + BIRD_RADIUS < self.pipe_x + PIPE_WIDTH:
            if not (self.pipe_gap_y < self.bird_y < self.pipe_gap_y + GAP_HEIGHT):
                self.done = True

        reward = 1 if not self.done else -100
        return self.get_state(), reward, self.done

    def render(self):
        if not self.render_mode:
            return
        self.screen.fill(WHITE)
        # Draw bird
        pygame.draw.circle(self.screen, BLUE, (50, int(self.bird_y)), BIRD_RADIUS)
        # Draw pipe
        pygame.draw.rect(self.screen, GREEN, (self.pipe_x, 0, PIPE_WIDTH, self.pipe_gap_y))
        pygame.draw.rect(self.screen, GREEN, (self.pipe_x, self.pipe_gap_y + GAP_HEIGHT, PIPE_WIDTH, HEIGHT))
        pygame.display.flip()
        self.clock.tick(FPS)

if __name__ == "__main__":
    env = FlappyBirdEnv(render=True)
    state = env.reset()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        action = 1 if pygame.key.get_pressed()[pygame.K_SPACE] else 0
        state, reward, done = env.step(action)
        env.render()

        if done:
            state = env.reset()

    pygame.quit()
    sys.exit()
