#Author: Patrick
#SHAPES PROGRAM
import pygame,time
pygame.init()

#Create Canvas
surface = pygame.display.set_mode([700,700])

#Set Retangle & Colour Variables
box = pygame.Rect(160,300,100,100)
colorRED = pygame.Color("red")
colorBLACK = pygame.Color("black")
colorBLUE = pygame.Color("blue")

#Fill Canvas
surface.fill(colorBLUE)

#Draw Circle & Triangle
pygame.draw.circle(surface,colorBLACK, [0,0],200)
pygame.draw.polygon(surface,colorBLACK,[[400,375],[425,425],[375,425]])

#Draw Rectangle
rect = pygame.Rect(200 200,100,40)
pygame.draw.rect(surface, colorRED, rect)

#Display Whats in Memory
pygame.display.flip()
time.sleep(30)
pygame.display.quit()
