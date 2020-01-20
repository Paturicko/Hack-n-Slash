#Author: Patrick
#FROG MOVEMENT PROGRAM
import pygame,time
pygame.init()

#Display Surface & Set Colour Variables
surface = pygame.display.set_mode([700,700])
bcolour = pygame.Color("blue")
colorGREEN = pygame.Color("green")

#Import Sprites
pygame.draw.circle(surface,colorGREEN,[200,200],30)
img = pygame.image.load("FroggieLeft.png")
imgLEFT = pygame.image.load("FroggieLeft.png")
imgRIGHT = pygame.image.load("FroggieRight.png")
imgUP = pygame.image.load("FroggieUp.png")
imgDOWN = pygame.image.load("FroggieDown.png")

#Frog X, Y & speed
x = 100
y = 100
speed = 10

while True:
    #Check for QUIT
    if pygame.event.peek(pygame.QUIT):
        pygame.diisplay.quit()
        quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        y = y - speed
        img = imgUP
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        y = y + speed
        img = imgDOWN
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x = x - speed
        img = imgLEFT
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x = x + speed
        img = imgRIGHT

    #Draw Screen
    surface.fill(bcolour)
    surface.blit(img,[x,y])
    pygame.display.flip()

    #Pause
    time.sleep(1/60)
pygame.display.quit