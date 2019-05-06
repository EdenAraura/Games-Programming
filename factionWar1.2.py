##Importing Modules
import pygame, random, time, os, sys
from pygame.locals import *

pygame.init()

#Set-Up - Dimensions, Fullscreen, caption, time
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Faction Wars")
clock = pygame.time.Clock()

#Images
playerImg = pygame.image.load(os.path.join("assets", "playerShip.png"))
enemyImg = pygame.image.load(os.path.join("assets", "enemyShip.png"))
missileImg = pygame.image.load(os.path.join("assets", "missile.png"))
background = pygame.image.load(os.path.join("assets", "background.png"))

#Sounds
fireSound = pygame.mixer.Sound(os.path.join("assets", "laser6.wav"))
music = pygame.mixer.music.load(os.path.join("assets", "Hypnotic-Puzzle.wav"))
pygame.mixer.music.play(-1)

font = pygame.font.SysFont("comicsansms", 72)
deadText = ("You died! Press escape to exit")

y = 0

deadState = False

ammo = 50
ammoCount = ("Ammo: {0}".format(ammo))

#Classes
#Player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImg
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 1920 / 2
        self.rect.bottom = 1080 - self.rect.y - 2
        self.speedx = 3

    #moving player & keeping them on screen
    def update(self):
        self.speedx = 0

        keystate = pygame.key.get_pressed()

        if inpt[K_a]:
            self.speedx = -5
        if inpt[K_d]:
            self.speedx = 5

        self.rect.x += self.speedx

        if self.rect.right > 1920:
            self.rect.right = 1920
        if self.rect.left < 0:
            self.rect.left = 0

    #firing missile
    def fire(self):
        global ammo
        if(ammo >= 1):
            fireSound.play()
            ammo -= 1
            b = Missile(self.rect.centerx, self.rect.top)
            bullets.add(b)
            sprites.add(b)

#enemy
class Enemy(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = enemyImg
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0,1920)
		self.rect.y = 0
		self.yspeed = random.randint(1,2)
		self.xspeed = random.randint(-2,2)

    #speed,spawning, keeping on screen
	def update(self):
		self.rect.y += self.yspeed
		self.rect.x += self.xspeed

		if self.rect.top > 1080:
			self.rect.x = random.randint(0,1920)
			self.rect.y = 0
			self.yspeed = random.randint(1,2)
			self.xspeed = random.randint(-2,2)

		if self.rect.right > 1080 or self.rect.left < 0:
			self.xspeed *= -1

#bullet
class Missile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = missileImg
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.yspeed = -3

    def update(self):
        self.rect.y += self.yspeed

player = Player()

sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

sprites.add(player)

for i in range(6):
	e = Enemy()
	enemies.add(e)
	sprites.add(e)

gameOn = True

while gameOn:

    inpt = pygame.key.get_pressed()

    y += 1

    clock.tick(50)

    #scrolling background
    rel_y = y % background.get_rect().height
    screen.blit(background, (0, y - 1080))
    if(y > 0):
        screen.blit(background, (0, rel_y))

    #loss condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

    if inpt[K_ESCAPE]:
        sys.exit()

    if pygame.sprite.spritecollide(player, enemies, True):
        deadState = True
        #sys.exit()

    if deadState == True:
        screen.fill((0,0,0))
        screen.blit(font.render(deadText,True, (0,0,255)),(450,500))
        for x in enemies:
            x.kill()

    sprites.update()
    enemies.update()
    bullets.update()

    #shooting enemy
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)

    for hit in hits:
        e = Enemy()
        enemies.add(e)
        sprites.add(e)
        ammo += 15

    if inpt[K_SPACE]:
        player.fire()

    sprites.draw(screen)
    screen.blit(font.render("Ammo: {0}".format(ammo),True, (0,0,255)),(10,10))

    pygame.display.flip()
