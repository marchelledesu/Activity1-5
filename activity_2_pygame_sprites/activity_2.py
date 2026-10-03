import random
import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Activity 2: Sprite System & Collision Arena")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (44, 94, 138), (20, 20), 20)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((28, 28), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (180, 60, 60), (14, 14), 14)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.direction = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.direction *= -1
            self.rect.x += self.speed * self.direction


all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for _ in range(7):
    enemy = Enemy(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50), random.randint(2, 4))
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    enemies.update()

    collisions = pygame.sprite.spritecollide(player, enemies, True)
    if collisions:
        score += len(collisions)
        for _ in range(min(2, 7 - len(enemies))):
            if len(enemies) < 9:
                enemy = Enemy(random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40), random.randint(2, 5))
                all_sprites.add(enemy)
                enemies.add(enemy)

    screen.fill((17, 24, 39))
    all_sprites.draw(screen)

    label = font.render(f"Score: {score}", True, (220, 220, 220))
    screen.blit(label, (10, 10))

    pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    pass
