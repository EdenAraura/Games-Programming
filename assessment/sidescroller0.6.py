import pygame,sys,random,os,time
from pygame.locals import *

xPos = 960
yPos = 900
positionX = 300
positionY = 300

playerLeft = False
playerRight = False

playerpos = 0

pygame.init()
pygame.display.set_caption("uwu")

walkLeft = pygame.image.load(os.path.join("assets", "pcLeft.png"))
walkRight = pygame.image.load(os.path.join("assets", "pcRight.png"))
width = 100
height = 250

##creates canvas & declares it as "screen"
screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)

background = pygame.image.load(os.path.join("assets","greeceBackground.png"))

##Item Classes

class Player(pygame.sprite.Sprite):
    #img = pygame.image.load(os.path.join("assets", "pc.png"))
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("assets", "pc.png"))
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = self.image.get_rect()
        #self.rect.center = (self.x, self.y)
        self.hitbox = (self.x, self.y, self.w, self.h)

    def draw(self, screen):
        self.hitbox = (self.x, self.y, self.w, self.h)
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        #self.mask = pg.mask.from_surface(self.img)

class Soapbox:
    img = pygame.image.load(os.path.join("assets", "soapbox.png"))
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hitbox = (self.x, self.y, self.w, self.h)

    def draw(self, screen):
        self.hitbox = (self.x, self.y, self.w, self.h)
        screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        ##self.mask = pg.mask.from_surface(self.img)

class Luxury(Soapbox):
    img = pygame.image.load(os.path.join("assets", "luxury.png"))

    def draw(self, screen):
        self.hitbox = (self.x, self.y, self.w, self.h)
        screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        ##self.mask = pg.mask.from_surface(self.img)

##class Background(pygame.sprite.Sprite):
##    def __init__(self, imageFile, location):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.image.load(imageFile)
##        self.rect = self.image.get_rect()
##        self.rect.left, self.rect.top = location

##BackGround = Background('greeceBackground.png', [0,0])

##pygame.time.set_timer(USEREVENT+2, random.randrange(3000, 7000))

x = 0
soap = Soapbox(300, 0, 128, 64)
lux = Luxury(300, 300, 90, 28)
avatar = Player(960, 800, 100, 250)

objects = []

sprites = pygame.sprite.Group()
sprites.add(avatar)

while 1:
    #clock.tick(40)
    inpt = pygame.key.get_pressed()

    ##sprites.update()

    #screen.fill((79,3,56))
    rel_x = x % background.get_rect().width
    screen.blit(background, (rel_x - background.get_rect().width,0))
    if(rel_x < 1920):
        screen.blit(background, (rel_x, 0))

    avatar.draw(screen)
    #sprites.draw(screen)

    pygame.display.toggle_fullscreen()
    ## movable player
    ##avatar.draw(screen)
    #if playerLeft:
        #screen.blit(walkLeft (xPos, yPos))
    #elif playerRight:
        #screen.blit(walkRight(xPos, yPos))

    if inpt[K_a] and xPos >= 0:
        playerLeft = True
        playerRight = False
        x+=6
        playerpos -=1
        for item in objects:
            item.x += 5
    if inpt[K_d] and xPos <= 1280:
        playerLeft = False
        playerRight = True
        x-=6
        playerpos+=1
        for item in objects:
            item.x -= 5

    if playerpos <=-50 or playerpos >=50:
        playerpos = 0

    if playerpos == (random.randrange(-50,50)):
        r = random.randrange(0,2)
        if r == 0:
            objects.append(Soapbox(1940,970,128,64))
        elif r == 1:
            objects.append(Luxury(1940, 970, 90, 28))

    ##soap.draw(screen)
    ##lux.draw(screen)
    for item in objects:
        item.draw(screen)

    pygame.display.update()

    if inpt[K_ESCAPE]:
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        ##if event.type == USEREVENT + 2:
    ##        r = random.randrange(0,2)
        ##    if r == 0:
                ##objects.append(Soapbox(1940,970,128,64))
        ##    elif r == 1:
            ##    objects.append(Luxury(1940, 970, 90, 28))
