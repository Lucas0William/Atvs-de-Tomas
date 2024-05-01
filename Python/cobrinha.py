import pygame
import random

# Inicialização do pygame
pygame.init()

# Definições de cores

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configurações da tela
WIDTH, HEIGHT = 800, 600
FPS = 10

# Inicialização da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cobrinha")

# Variáveis do jogo
snake_pos = [(WIDTH // 2, HEIGHT // 2)]
snake_dir = (0, 0)
food_pos = (random.randint(0, WIDTH - 20) // 20 * 20, random.randint(0, HEIGHT - 20) // 20 * 20)

clock = pygame.time.Clock() 

# Função para desenhar a cobra e a comida
def draw_snake():
    for pos in snake_pos:
        pygame.draw.rect(screen, BLACK, (pos[0], pos[1], 20, 20))
    pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], 20, 20))

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, 1):
                snake_dir = (0, -1)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -1):
                snake_dir = (0, 1)
            elif event.key == pygame.K_LEFT and snake_dir != (1, 0):
                snake_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-1, 0):
                snake_dir = (1, 0)

    # Movimento da cobra
    new_head = (snake_pos[0][0] + snake_dir[0] * 20, snake_pos[0][1] + snake_dir[1] * 20)
    snake_pos.insert(0, new_head)
    if snake_pos[0] == food_pos:
        food_pos = (random.randint(0, WIDTH - 20) // 20 * 20, random.randint(0, HEIGHT - 20) // 20 * 20)
    else:
        snake_pos.pop()

    # Verificação de colisão
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT or len(snake_pos) != len(set(snake_pos)):
        running = False

    # Desenhar na tela
    screen.fill(WHITE)
    draw_snake()
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
