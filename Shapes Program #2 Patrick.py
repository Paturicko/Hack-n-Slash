# #Author: Patrick
#SHAPES PROGRAM #2
import pygame,time
pygame.init()

#Create Canvas
surface = pygame.display.set_mode([1000,1000])

#Colour Variables
colorRED = pygame.Color("red")
colorBLACK = pygame.Color("black")
colorBLUE = pygame.Color("blue")
colorGREEN = pygame.Color("green")

#Fill Canvas
surface.fill(colorBLACK)

#Draw Circle & Triangle
pygame.draw.circle(surface,colorGREEN, [600,300],50)
pygame.draw.polygon(surface,colorRED,[[550,450],[550,550],[500,550]])
pygame.draw.polygon(surface,colorRED,[[650,450],[700,550],[650,550]])

#Draw Rectangle
rect = pygame.Rect(450, 350,300,100)
pygame.draw.rect(surface, colorBLUE, rect)
rect2 = pygame.Rect(550, 450,100,100)
pygame.draw.rect(surface, colorBLUE, rect2)

#Display Whats in Memory
pygame.display.flip()
time.sleep(15)
pygame.display.quit()
