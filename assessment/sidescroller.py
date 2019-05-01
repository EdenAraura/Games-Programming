import pygame,sys,random,os
from pygame.locals import *

xPos = 1
yPos = 1
positionX = 300
positionY = 300

pygame.init()
pygame.display.set_caption("uwu")

##creates canvas & declares it as "screen"
screen = pygame.display.set_mode((1920,1080))

background = pygame.image.load("greeceBackground.png")

##Item Classes
class Background(pygame.sprite.Sprite):
    def __init__(self, imageFile, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('greeceBackground.png', [0,0])
while 1:
    #clock.tick(40)
    inpt = pygame.key.get_pressed()

    #screen.fill((79,3,56))
    screen.blit(BackGround.image, BackGround.rect)
    ## movable player
    pygame.draw.circle(screen,(3,3,75),(xPos,yPos),75,7)
    if inpt[K_LEFT] and xPos >= 0:
        xPos -= 1
    if inpt[K_RIGHT] and xPos <= 1280:
        xPos += 1
    if inpt[K_UP] and yPos >=0:
        yPos -= 1
    if inpt[K_DOWN] and yPos <= 720:
        yPos += 1

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
