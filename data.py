import pygame
import os

from random import randint,choice 
pygame.init()
size_window=(500, 600) 
size_background = (3000, 3000)
size_hero = (50, 50)
size_bot =(42, 48)
size_buff = (50,50)

BLACK=(5, 5,5)
BLACKS = (255,5,200)
WHITE= (255, 255, 255)
RED= (128,0,0)
GREEN =(100, 255, 100)
FPS = 60
COUNT_BUFF = 5
BUFFS = ["HP","speed_bullet","speed_shoot","imortal",'freezing']

heart_list= list()
bot_list= list()
bullet_list_hero = list()
bullet_list_bot = list()

abs_path=os.path.abspath(__file__ + "/..") 
hero_image_list =[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "spaceship1.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "spaceship2.png")), size_hero)
]
bot_image_list=[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "robbership1.png")), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "robbership2.png")), size_bot) 
]
    
#bot2_image_list=[
#pygame, transform.scale(pygame.image.load(os.path.join(abs_path, "image", "bot_red.png")), size_bot) 
#] 

background_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "space1.png")), size_background)
heart_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "heart.png")), [30,30])
skull_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "skull.png")), [30,30])

buff_images=[
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "b_heart.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "b_bullet_speed.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "b_bullet_limit.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "b_imortal.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "b_freezing.png")), size_buff)
]