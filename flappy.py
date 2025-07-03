import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
BIRD_RADIUS = 15
PIPE_WIDTH = 60
GAP_HEIGHT = 150
GRAVITY = 0.5
JUMP_STRENGTH = -8
FPS = 30

WHITE = (255, 255, 255)

class FlappyBirdEnv:
    def __init__(self, render=False):
        self.render_mode = render
        if render:
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
            self.clock = pygame.time.Clock()
            
            # Load sprites
            self.bird_img = pygame.image.load("assets/yellowbird.png")
            self.bird_img = pygame.transform.scale(self.bird_img, (30, 30))

            self.pipe_img = pygame.image.load("assets/pipe-green.png")
            self.pipe_img = pygame.transform.scale(self.pipe_img, (PIPE_WIDTH, HEIGHT))

            self.bg_img = pygame.image.load("assets/background-day.png")
            self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))

            self.digit_imgs = [pygame.image.load(f"assets/{i}.png").convert_alpha() for i in range(10)]

            self.base_img = pygame.image.load("assets/base.png").convert_alpha()
            self.base_y = HEIGHT - 20
            self.base_x = 0

            self.font = pygame.font.SysFont("Arial", 32)

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

        if action == 1:
            self.bird_vel = JUMP_STRENGTH
        self.bird_vel += GRAVITY
        self.bird_y += self.bird_vel

        self.pipe_x -= 5
        if self.pipe_x + PIPE_WIDTH < 0:
            self.pipe_x = WIDTH
            self.pipe_gap_y = random.randint(100, HEIGHT - 200)
            self.score += 1

        if self.bird_y < 0 or self.bird_y > HEIGHT:
            self.done = True
        if self.pipe_x < 50 + BIRD_RADIUS < self.pipe_x + PIPE_WIDTH:
            if not (self.pipe_gap_y < self.bird_y < self.pipe_gap_y + GAP_HEIGHT):
                self.done = True

        reward = 1 if not self.done else -100
        return self.get_state(), reward, self.done
    
    def draw_score(self):
        score_str = str(self.score)
        total_width = sum(self.digit_imgs[int(d)].get_width() for d in score_str)
        x = (WIDTH - total_width) // 2
        y = 50  # Adjust y as needed

        for d in score_str:
            digit_img = self.digit_imgs[int(d)]
            self.screen.blit(digit_img, (x, y))
            x += digit_img.get_width()
    
    def draw_game_over(self):
        # Dim background
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        # Game Over text
        font = pygame.font.SysFont("Arial", 48, bold=True)
        text = font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        self.screen.blit(text, text_rect)

        # Final score
        small_font = pygame.font.SysFont("Arial", 32)
        score_text = small_font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(score_text, score_rect)

        # Restart instruction
        restart_text = small_font.render("Press R to Restart", True, (200, 200, 200))
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)

        restart_text = small_font.render("Press ESC to Quit", True, (200, 200, 200))
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        self.screen.blit(restart_text, restart_rect)

        pygame.display.flip()


    def render(self):
        if not self.render_mode:
            return

        self.screen.blit(self.bg_img, (0, 0))
        self.screen.blit(self.pipe_img, (self.pipe_x, self.pipe_gap_y + GAP_HEIGHT))
        top_pipe = pygame.transform.flip(self.pipe_img, False, True)
        self.screen.blit(top_pipe, (self.pipe_x, self.pipe_gap_y - HEIGHT))

        self.screen.blit(self.bird_img, (50, int(self.bird_y)))

        self.base_x -= 5
        if self.base_x <= -self.base_img.get_width():
            self.base_x += self.base_img.get_width()
        self.screen.blit(self.base_img, (self.base_x, self.base_y))
        self.screen.blit(self.base_img, (self.base_x + self.base_img.get_width(), self.base_y))

        # Score display
        self.draw_score()

        pygame.display.flip()
        self.clock.tick(FPS)
