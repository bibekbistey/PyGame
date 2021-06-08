import pygame
x= pygame.init()

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
#creating window
gameWindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("My first Game")
#Game specific variables
exit_game=False
game_over=False

#creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("you have pressed right key")

gameWindow.fill(white)
pygame.display.update()
pygame.quit()
quit()
