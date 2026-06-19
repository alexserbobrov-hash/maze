#создай игру "Лабиринт"!
from pygame import *

window = display.set_mode((1400, 1000))
display.set_caption('Лабиринт')

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, speed, x_cor, y_cor):
        self.image = transform.scale(image.load(sprite_image), (100, 100))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class PlayerSprite(GameSprite):
    def move(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed  
        elif keys[K_DOWN] and self.rect.y < 895:
            self.rect.y += self.speed 
        elif keys[K_RIGHT] and self.rect.x < 1295:
            self.rect.x += self.speed  
        elif keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed  

class Enemy(GameSprite):
    right = True
    def update(self):
        if self.rect.x > 1100:
            self.right = False
        if self.rect.x < 670:
            self.right = True
        if self.right:
            self.rect.x += self.speed 
        elif self.right == False:
            self.rect.x -= self.speed 

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

walls = []

wall_1 = Wall(165, 52, 1, 600, 200, 50, 800)
walls.append(wall_1)
wall_2 = Wall(165, 52, 1, 600, 400, 450, 50)
walls.append(wall_2)
wall_3 = Wall(165, 52, 1, 800, 0, 50, 250)
walls.append(wall_3)
wall_4 = Wall(165, 52, 1, 1200, 0, 50, 800)
walls.append(wall_4)
wall_5 = Wall(165, 52, 1, 1100, 600, 100, 50)
walls.append(wall_5)
wall_6 = Wall(165, 52, 1, 900, 600, 50, 400)
walls.append(wall_6)
wall_7 = Wall(165, 52, 1, 1025, 850, 50, 150)
walls.append(wall_7)


background = transform.scale(image.load('Media/background.jpg'), (1400, 1000))
cyborg = Enemy('Media/cyborg.png', 8, 1200, 500)
hero = PlayerSprite('Media/hero.png', 10, 400, 300)
treasure = GameSprite('Media/treasure.png', 10, 1275, 50)

game = True

font.init()

font = font.Font(None, 108)
win_text = font.render('YOU WIN!', True, (255, 255, 15))
lose_text = font.render('YOU LOSE!', True, (150, 21, 0))


clock = time.Clock()
mixer.init()

mixer.music.load('Media/jungles.ogg')
mixer.music.play()

kick = mixer.Sound('Media/kick.ogg')

money = mixer.Sound('Media/money.ogg')

#finish = False
lose = False
win = False

while game:
    window.blit(background, (0, 0))

    for events in event.get():
        if events.type == QUIT:
            game = False

    for element in walls:
        element.draw_wall()

    #if finish != True:
    if lose != True and win != True:

        for element in walls:
            element.draw_wall()
            if sprite.collide_rect(hero, element):
                finish = True
                kick.play()
                lose = True

        if sprite.collide_rect(hero, cyborg):
                finish = True
                kick.play()
                lose = True

        if sprite.collide_rect(hero, treasure):
                finish = True
                money.play()
                win = True
    
        cyborg.reset()
        hero.reset()
        treasure.reset()
        if lose == True:
            window.blit(lose_text, (500, 465))
        if win == True:
            window.blit(win_text, (500, 465))

        cyborg.update()
        hero.move()

        for events in event.get():
            if events.type == QUIT:
                game = False
        
        clock.tick(60)
        display.update()