from data import *

class Plane(pygame.Rect):
    def __init__(self,x,y,width,height,image_list,step):
        super().__init__(x,y,width,height)
        self.image_list = image_list
        self.image = self.image_list[0]
        self.image_count = 0
        self.step = step

    def move_image(self):
        if self.image_count == len(self.image_list * 10) - 1:
            self.image_count = 0
        if self.image_count % 10 == 0:
            self.image = self.image_list[self.image_count // 10]
        self.image_count+=1

class Hero (Plane):
    def __init__(self,x,y,width,height,image_list,step,hp):
        super().__init__(x,y,width,height,image_list,step)
        self.walk = {"left":False,"right":False}
        self.hp = hp
        self.start_x = x
        self.start_y = y
        self.time_shoot = 0
        self.can_shoot = True
        self.kill_bot = 0

    def move(self,window):
        if self.walk["left"] and self.x > 0:
            self.x -= self.step
        if self.walk["right"] and self.x < size_window[0]:
            self.x += self.step

        if True in list(self.walk.values()):
            self.move_image()
        else:
            self.image = self.image_list[0]
        window.blit(self.image, (self.x, self.y))
        self.shoot()

    def shoot(self):
        self.time_shoot += 1
        if self.time_shoot > FPS // 2:
            self.can_shoot = True
            self.time_shoot = 0

    def collide_enemy(self, objects):
        index = self.collidelist(objects)
        if index != -1:
            self.hp -= 1
            objects.pop(index)

    #def collide_buff(self,buff_list):




class Bot(Plane):
    def __init__(self,x,y,width,height,image_list,step):
        super().__init__(x,y,width,height,image_list,step)
        self.start_x = x
        self.start_y = y
        self.start_time = 0
        self.random_time = randint(1500,2500)

    def move(self,window): 
        self.y += self.step
        window.blit(self.image, (self.x, self.y)) 

    def shoot(self, time_bot):
        if time_bot - self.start_time > self.random_time:
            self.start_time = time_bot
            self.random_time = randint(1500,2500)
            bullet_list_bot.append(Bullet(self.centerx -5, self.bottom - 20, 10, 20, GREEN, 4, None))

    def collide(self, objects):
        index = self.collidelist(objects)
        if index != -1:
            bot_list.remove(self)
            objects.pop(index)
            return True
        return False
    



class Bullet(pygame.Rect):
    def __init__(self,x,y,width,height,color,step,image= None):
        super().__init__(x,y,width,height)
        self.color = color
        self.image = image
        self.start_x = x
        self.start_y = y
        self.step = step
    
    def move(self,window):
        self.y += self.step
        pygame.draw.rect(window, self.color, self)
        #window.blit(self.image, (self.x, self.y))

class Buff(pygame.Rect):
    def __init__(self,x,y,width,height,image,designed,step):
        super().__init__(x,y,width,height)
        self.image = image
        self.designed = designed
        self.step = step

    def move(self,window):
        self.y += self.step
        window.blit(self.image,(self.x,self.y))

class Background(pygame.Rect):
    def __init__(self, height, image, step):
        self.y1 = 0
        self.y2 = -height
        self.height = height
        self.step = step
        self.image1 = image
        self.image2 = image

    def move(self,window):
        self.y1 += self.step
        self.y2 += self.step

        if self.y1 >= size_window[1]:
            self.y1 = - self.height
        if self.y2 >= size_window[1]:
            self.y2 = - self.height
        
        window.blit(self.image1,(0,self.y1))
        window.blit(self.image2,(0,self.y2))

                