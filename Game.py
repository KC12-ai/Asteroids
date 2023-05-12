import pygame
import math
import random
pygame.init()

# Set up the game window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Asteroids")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Load images
ship_image = pygame.image.load("ship.png")
asteroid_images = []
asteroid_images.append(pygame.image.load("Asteroid1.png"))
asteroid_images.append(pygame.image.load("Asteroid2.png"))
asteroid_images.append(pygame.image.load("Asteroid3.png"))

# Define classes
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ship_image
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.centery = height/2
        self.speed = 0
        self.angle = 0

    def update(self):
        # Rotate the ship
        self.image = pygame.transform.rotate(ship_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Move the ship
        x = self.rect.centerx + self.speed * math.cos(math.radians(self.angle))
        y = self.rect.centery - self.speed * math.sin(math.radians(self.angle))
        self.rect.center = (x, y)

        # Wrap around the screen
        if self.rect.right < 0:
            self.rect.left = width
        elif self.rect.left > width:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = height
        elif self.rect.top > height:
            self.rect.bottom = 0
Ship()
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = asteroid_images[random.randint(0, 2)]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = random.randint(1, 3)
        self.angle = random.randint(0, 360)
        self.size = size

    def update(self):
        # Rotate the asteroid
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Move the asteroid
        x = self.rect.centerx + self.speed * math.cos(math.radians(self.angle))
        y = self.rect.centery - self.speed * math.sin(math.radians(self.angle))
        self.rect.center = (x, y)

        # Wrap around the screen
        if self.rect.right < 0:
            self.rect.left = width
        elif self.rect.left > width:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = height
        elif self.rect.top > height:
            self.rect.bottom = 0
asteroid=Asteroid(5, 6, 7)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((3, 3))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 10
        self.angle = angle

    def update(self):
        # Move the bullet
        x = self.rect.centerx + self.speed * math.cos(math.radians(self.angle))
bull=Bullet(1, 1, 1)
