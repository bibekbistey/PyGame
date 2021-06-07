import pygame
x= pygame.init()
GameWindow=pygame.display.set_mode((1200,500))
pygame.display.set_caption("My second game")
exit_game=False
game_over=False
while not exit_game:
    for event in pygame.event.get():
        print(event)
pygame.quit()
quit()