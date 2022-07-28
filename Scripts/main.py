import pygame as g
from os import system

g.init()
win = g.display.set_mode((1080, 720))

g.display.set_caption("Game")

bg = g.image.load('D:\Programs\WorkSpaces\Python\Game\Content\player\S_background.jpg')

Player = g.image.load('D:\Programs\WorkSpaces\Python\Game\Content\player\Sprite4.png')

Clock = g.time.Clock()

x = 1020
y = 600
widht = 80
height = 80
speed = 8
player_tick = 0

IsJump = False
JumpCount = 10

#left = False
#right = False
#animCount = 0
#lastmove = "right"
facing = -1

class bullet():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 5 * facing

    def draw(self, win):
        g.draw.circle(win, self.color, (self.x, self.y), self.radius)

def drawWindow():
    global player_tick

    win.blit(bg, (0, 0))

    if player_tick + 1 >= 60:
        player_tick = 0
    else:
        win.blit(Player, (x, y))

    for bullet_obj in bullets:
        bullet_obj.draw(win)

    g.display.update()


run = True
bullets = []
while run:
    Clock.tick(60)

    for event in  g.event.get():
        if event.type == g.QUIT:
            run = False

    for bullet_obj in bullets:
        if bullet_obj.y < 720 and bullet_obj.y > 0:
            bullet_obj.y += bullet_obj.vel
        else:
            bullets.pop(bullets.index(bullet_obj))

    keys = g.key.get_pressed()

    if keys[g.K_f]:
        if len(bullets) < 5:
            bullets.append(bullet(round(x + widht // 2), round(y + height // 2), 5, (255, 255, 5), facing))
#        if lastmove == "right":   
#           facing = 1
#       else: facing = -1
    if keys[g.K_UP]:
        y -= speed
    if keys[g.K_DOWN]:
        y += speed
    if keys[g.K_LEFT] and x > 5:
        x -= speed
#        lastmove = "right"
    if keys[g.K_RIGHT] and x < 1080 - widht - 5:
        x += speed
#        lastmove = "right"
    if not(IsJump):    
        if keys[g.K_SPACE]:
            IsJump = True
    else:
        if JumpCount >= -10:
            if JumpCount < 0:
                y +=(JumpCount ** 2) / 2
            else:
                y -= (JumpCount ** 2) / 2
            JumpCount -= 1
        else:
            IsJump = False
            JumpCount = 10

    drawWindow()

g.quit()