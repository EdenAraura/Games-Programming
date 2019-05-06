import pygame, random, time, os, sys
from pygame.locals import *

		# PYGAME SETUP AND INITIALISATION
pygame.init()

# -- Global constants

# COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# Screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.FULLSCREEN)
pygame.display.set_caption("Faction Wars")
clock = pygame.time.Clock()

# Loading images and converting where appropriate
playerImg = pygame.image.load(os.path.join("assets", "playerShip.png"))
playerImg.set_colorkey((255,255,255))
img2 = pygame.image.load(os.path.join("assets", "enemyShip.png"))
img3 = pygame.image.load(os.path.join("assets", "missile.png"))

background = pygame.image.load(os.path.join("assets", "background.png"))
y = 0

shootTime = 0
shootCounter = 0

		## CLASS DECLEARATIONS (AKA BLUEPRINTS) ##

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImg
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - self.rect.y - 2
        self.speedx = 3

    def update(self):
        self.speedx = 0

        keystate = pygame.key.get_pressed()

        if inpt[K_a]:
            self.speedx = -5
        if inpt[K_d]:
            self.speedx = 5

        self.rect.x += self.speedx

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def fire(self):
        global shootCounter
        if shootCounter <= 5:
            shootTime = pygame.time.get_ticks()
            f = Missile(self.rect.centerx, self.rect.top)
            bullets.add(f)
            all_sprites_list.add(f)
            shootCounter += 1
            print(shootCounter)


class Enemy(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = img2
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0,1920)
		self.rect.y = 0
		self.yspeed = random.randint(1,2)
		self.xspeed = random.randint(-2,2)

	def update(self):
		self.rect.y += self.yspeed
		self.rect.x += self.xspeed

		if self.rect.top > SCREEN_HEIGHT:
			self.rect.x = random.randint(0,1920)
			self.rect.y = 0
			self.yspeed = random.randint(1,2)
			self.xspeed = random.randint(-2,2)

		if self.rect.right > 800 or self.rect.left < 0:
			self.xspeed *= -1

class Missile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img3
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.yspeed = -3

    def update(self):
        self.rect.y += self.yspeed


		## INSTANTIATIONS / GLOBAL VARIABLES

player = Player()


all_sprites_list = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites_list.add(player)


for i in range(6):
	e = Enemy()
	enemies.add(e)
	all_sprites_list.add(e)


gameOn = True


				## MAIN LOOP
while gameOn:

    inpt = pygame.key.get_pressed()

    y += 1

    clock.tick(50)
    currentTime = pygame.time.get_ticks()

    if currentTime - shootTime >= 5000:
        print("5 seconds")
        #shootTime -= shootTime
        #shootCounter = 0
    #print(currentTime)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        if inpt[K_ESCAPE]:
            sys.exit()

    rel_y = y % background.get_rect().height
    screen.blit(background, (0, y - 1080))
    if(y > 0):
        #print(y)
        screen.blit(background, (0, rel_y))

    all_sprites_list.update()
    enemies.update()
    bullets.update()

    if pygame.sprite.spritecollide(player, enemies, True):
        gameOn = False

    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        e = Enemy()
        enemies.add(e)
        all_sprites_list.add(e)

    if inpt[K_SPACE]:
        player.fire()

    #screen.fill(BLACK)
    all_sprites_list.draw(screen)

    pygame.display.flip()
