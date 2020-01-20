#Author: Patrick
#TREE DRAWING PROGRAM
import pygame,time
pygame.init()

#Display Surface & Set Colour Variables
surface = pygame.display.set_mode([1300,1300])
green = pygame.Color("green")
brown = pygame.Color("brown")
Blue = pygame.Color("blue")
surface.fill(Blue)

#Draw Shapes
stump = pygame.Rect(400,700,100,300)
pygame.draw.polygon(surface,green,[[300,300],[500,100],[700,300]])
pygame.draw.polygon(surface,green,[[300,500],[500,300],[700,500]])
pygame.draw.polygon(surface,green,[[300,700],[500,500],[700,700]])
pygame.draw.rect(surface,brown,stump)

#Display Screen
pygame.display.flip()
time.sleep(30)
pygame.display.quit