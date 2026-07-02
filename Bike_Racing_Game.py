import pygame
import random

pygame.init()
pygame.mixer.init()

# Screen
width = 600
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Dark Racing Game")

# Load background image
road = pygame.image.load("road.png")
road = pygame.transform.scale(road, (width, height))

# Load sounds
engine_sound = pygame.mixer.Sound("engine.wav")
crash_sound = pygame.mixer.Sound("crash.wav")
engine_sound.play(-1)  # loop engine sound

# Colors
white = (255, 255, 255)
red = (200, 0, 0)
blue = (0, 100, 255)

# Player car
car_width = 50
car_height = 100
car_x = width // 2 - car_width // 2
car_y = height - 150
car_speed = 7

# Enemy car
enemy_width = 50
enemy_height = 100
enemy_x = random.randint(100, width - 150)
enemy_y = -100
enemy_speed = 6   # constant speed (no increase)

clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    clock.tick(60)

    screen.blit(road, (0, 0))  # draw background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 100:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < width - 150:
        car_x += car_speed

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > height:
        enemy_y = -100
        enemy_x = random.randint(100, width - 150)
        score += 1

    # Collision
    if (car_x < enemy_x + enemy_width and
        car_x + car_width > enemy_x and
        car_y < enemy_y + enemy_height and
        car_y + car_height > enemy_y):
        crash_sound.play()
        pygame.time.delay(1000)
        running = False

    # Draw cars
    pygame.draw.rect(screen, blue, (car_x, car_y, car_width, car_height))
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_width, enemy_height))

    # Score
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
