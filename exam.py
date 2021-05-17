import pygame
import os

pygame.init()
surface = pygame.display.set_mode((900, 630))
img1 = pygame.image.load("images/player1.jpg")
# img1 = pygame.transform.scale(img1, (500, 330))
img2 = pygame.image.load("label.jpeg")
# img1 = pygame.transform.scale(img1, (500, 330))
while True:
    surface.blit(img1, (0, 0))
    pygame.display.update()
    position = pygame.mouse.get_pos()
    if  592 >=position[0]>= 336 and  344<= position[1] <=399:
        surface.blit(img2, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
        if event.type == pygame.QUIT:
            exit()