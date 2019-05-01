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

luxImg = pygame.image.load(os.path.join("assets", "luxury.png"))
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
        self.rect.x = x
        self.rect.y = y
        #self.rect.center = (self.x, self.y)
        self.hitbox = (self.x, self.y, self.w, self.h)

    def update(self):
        self.rect = self.rect

    def draw(self, screen):
        self.hitbox = (self.x, self.y, self.w, self.h)
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
        #self.mask = pg.mask.from_surface(self.img)

    def detectSoap(self):
        pygame.draw.rect(screen, (200, 30, 30), (200, 150, 100, 50), 0)

    def noSoap(self):
        pygame.draw.rect(screen, (0, 0, 0), (200, 150, 100, 50), 0)

class Soapbox(pygame.sprite.Sprite):
    #img = pygame.image.load(os.path.join("assets", "soapbox.png"))
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("assets", "soapbox.png"))
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hitbox = (self.x, self.y, self.w, self.h)

    def draw(self, screen):
        self.rect = (self.x, self.y, self.w, self.h)
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
        ##self.mask = pg.mask.from_surface(self.img)

class Luxury(Soapbox):
    #self.image = pygame.image.load(os.path.join("assets", "luxury.png"))
    #self.rect = self.image.get_rect()
    #img = pygame.image.load(os.path.join("assets", "luxury.png"))

    def draw(self, screen):
        self.hitbox = (self.x, self.y, self.w, self.h)
        screen.blit(luxImg, (self.x, self.y))
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
errorMessage = []

sprites = pygame.sprite.Group()
sprites.add(avatar)
sprites.add(soap)

while 1:
    #clock.tick(40)
    inpt = pygame.key.get_pressed()

    sprites.update()

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
            objects.append(Soapbox(1900,920,128,64))
        elif r == 1:
            objects.append(Luxury(1940, 970, 90, 28))

    ##soap.draw(screen)
    ##lux.draw(screen)
    for item in objects:
        item.draw(screen)

##    if avatar.y < soap.hitbox[1] + soap.hitbox[3] and avatar.y > soap.hitbox[1]:
##        if avatar.x > soap.hitbox[0] and avatar.x < soap.hitbox[0] + soap.hitbox[2]:
##            avatar.detectSoap()

    #pygame.Rect.colliderect(avatar.hitbox, soap.hitbox, True)
    #if pygame.sprite.spritecollide(avatar, soap, True):
    #if pygame.Rect.colliderect(avatar.image.get_rect(), soap.image.get_rect(), True):
    #if pygame.sprite.groupcollide(avatar, soap, True, True):
    #if pygame.sprite.collide_rect(avatar.rect, soap.rect):
    if avatar.rect.colliderect(soap.get_rect()):
        screen.fill((0,0,255))
    #elif not pygame.sprite.collide_rect(avatar, soap):
        #avatar.noSoap()
        #pygame.draw.rect(screen, (200, 30, 30), (200, 150, 100, 50), 0)

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
