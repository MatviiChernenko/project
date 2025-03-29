from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("MAZE")

clock = pygame.time.Clock()

hero = Hero(
    10,
    59,
    size_hero[0],
    size_hero[1],
    hero_image_list,
    3,
    3
)

snake = Snake(
    50,
    400,
    size_snake[0],
    size_snake[1],
    snake_image_list.copy(),
    5
)

slime = Slime(
    350,
    375,
    size_slime[0],
    size_slime[1],
    slime_image_list,
    4,
    "horizontal",
    radius= 155
)

slime1 = Slime(
    360,
    320,
    size_slime[0],
    size_slime[1],
    slime_image_list,
    8,
    "horizontal",
    radius= 145
)

slime2 = Slime(
    805,
    138,
    size_slime[0],
    size_slime[1],
    slime_image_list,
    4,
    "horizontal",
    radius= 150
)

gun = Gun(
    907,
    168,
    size_gun[0],
    size_gun[1],
    gun_image_list,
    0
)

gun1 = Gun(
    757,
    168,
    size_gun[0],
    size_gun[1],
    gun_image_list,
    0
)

fireball = Fireball(
    gun.x + 5,
    gun.y + 5,
    size_fireball[0],
    size_fireball[1],
    fireball_image_list,
    8,
    "vertical"
)

fireball1 = Fireball(
    gun1.x  + 5,
    gun1.y + 5,
    size_fireball[0],
    size_fireball[1],
    fireball_image_list,
    5,
    "vertical"
)

door = Door(
    825,
    452,
    size_door[0],
    size_door[1],
    door_image_list
)


slime_list.append(slime)
slime_list.append(slime1)
slime_list.append(slime2)
heart_list.append(Heart(934,452,50,50,heart_gold_image_list))
door_list.append(Door(900,452,50,50,door_image_list))


font = pygame.font.Font(None,40)

game = True
while game:
    if hero.hp <=0:
        game = False
    events = pygame.event.get()
    window.fill(BLACK)

    window.blit(heart_image_list,(3,3))
    render_hp = font.render(f"x{hero.hp}",True,WHITE)
    window.blit(render_hp,(22,5))

    #x,y = 0,0

    #for i in range(85):
     #   pygame.draw.line(window,WHITE, (0,y), (size_window[0], y))
      #  pygame.draw.line(window,WHITE, (x,0), (x, size_window[1]))
     #   x+=15
      #  y+=15

    hero.move(window)
    #snake.move(window)
    slime.guardion(window)
    slime1.guardion(window)
    slime2.guardion(window)
    door.blit(window)
    gun.striker(window,fireball)
    gun1.striker(window,fireball1)
      
    for wall in wall_list:
        pygame.draw.rect(window,wall.color,wall)
    

    for heart in heart_list:
        heart.blit(window)
        heart.collide_hero(hero)

    for slime in slime_list:
        slime.collide_hero(hero)

    hero.collide_heart(heart_list)

    for event in events:
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hero.walk["up"] = True
            if event.key == pygame.K_s:
                hero.walk["down"] = True
            if event.key == pygame.K_a:
                hero.walk["left"] = True
            if event.key == pygame.K_d:
                hero.walk["right"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hero.walk["up"] = False
            if event.key == pygame.K_s:
                hero.walk["down"] = False
            if event.key == pygame.K_a:
                hero.walk["left"] = False
            if event.key == pygame.K_d:
                hero.walk["right"] = False


    clock.tick(FPS)
    pygame.display.flip()