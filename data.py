import pygame
import os

from random import randint 
pygame.init()
size_window=(500, 600) 
size_background = (600, 3000)
size_hero = (70, 50)
size_bot =(42, 48)

BLACK=(5, 5,5)
BLACKS = (255,5,200)
WHITE= (255, 255, 255)
RED= (128,0,0)
GREEN =(100, 255, 100)
FPS = 60

heart_list= list()
bot_list= list()
bullet_list_hero = list()
bullet_list_bot = list()

abs_path=os.path.abspath(__file__ + "/..") 
hero_image_list =[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "test.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "test.png")), size_hero)
]
bot_image_list=[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "test.png")), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "test.png")), size_bot) 
]
    
#bot2_image_list=[
#pygame, transform.scale(pygame.image.load(os.path.join(abs_path, "image", "bot_red.png")), size_bot) 
#] 

background_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "test.png")), size_background)
heart_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "test.png")), [30,30])