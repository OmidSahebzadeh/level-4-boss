# init pygame
import pygame
pygame.init ()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Fight the Professor')
clock = pygame.time.Clock()
FPS = 60

# handige kleuren voor de game

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# De game

running = True
while running:
    # loop running at contstant fps
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        #kijken of game wordt afgesloten
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLUE)
    #after drawing everything
    pygame.display.flip()

pygame.quit()



