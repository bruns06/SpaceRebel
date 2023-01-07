import pygame
from pygame.locals import *
from sys import exit
import math
import random

#Basics
pygame.init()
SCR_WIDTH, SCR_HEIGHT = 1366, 768
SCREEN = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_caption('Space Rebel')
titleBkg = pygame.image.load('assets/Bkg.png')
lvBkg = pygame.image.load('assets/Bkg2.png')
heroImg = pygame.image.load('assets/Hero.png')
heroImg = pygame.transform.scale(heroImg, (250, 250))
bulletImg = pygame.image.load('assets/Bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (500, 500))
icon = pygame.image.load('assets/logo.ico')
enemy_list = []
enemy_img = pygame.image.load('assets/Enemy.png')
SPAWNENEMY = pygame.USEREVENT
pygame.time.set_timer(SPAWNENEMY,1000)
pygame.display.set_icon(icon)
lastTimeStamp = pygame.time.get_ticks()
hp = 5
bullet = 90
bullet_list = []
index = 0
score = 0
introS = True
lv1 = True
clock = pygame.time.Clock()

#Fonts
fnt = pygame.font.SysFont('Times New Roman', 48, bold=False, italic=True)

#Classes
class Hero:
    def __init__(self, sprite, Hp, x, y, bullet):
        self.sprite = sprite
        self.hp = Hp
        self.x = x
        self.y = y
        self.bullet = bullet 
    def update(self, Screen):
        SCREEN.blit(self.sprite, (self.x, self.y))
class BulletM:
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.x = x
        self.y = y
    def update(self, Screen):
        SCREEN.blit(self.sprite, (self.x, self.y))
class Enemy:
    def __init__(self, sprite, xVal, Size):
        self.sprite = sprite
        self.xVal = random.randint(0, 700)
        self.Size = random.randint(10, 400)
#Methods         
def intro():
    global introS
    titleTxtCLR = (222, 82, 73)
    titletxt = fnt.render('Start Game', True, titleTxtCLR)
    subtitletxt = fnt.render('Press Space Bar', True, titleTxtCLR)
    SCREEN.blit(titleBkg, (0, 0))
    SCREEN.blit(titletxt, (300, 300))
    SCREEN.blit(subtitletxt, (SCR_WIDTH/2 - 200, 600))
    mouseposx, mouseposy = pygame.mouse.get_pos()
    titletxt_RECT = titletxt.get_rect(topleft=(300, 300))
    #hoover = pygame.Rect.colliderect(titletxt_RECT, (mouseposx, mouseposy))
    while introS:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if e.key == K_SPACE:
                    introS = False
        clock.tick(60)
        pygame.display.update()
def Lv1():
    global bullet
    lifeTxt = fnt.render(f'Life : {hp}', False, 'white')
    scoreTxt = fnt.render(f'Score : {score}', False, 'white')
    pygame.display.set_caption('Level 1')
    playerStartPosX = SCR_WIDTH/2
    playerStartPosY = SCR_HEIGHT - 300
    Player = Hero(heroImg, hp, playerStartPosX, playerStartPosY, 5)
    X = Player.x
    Y = Player.y
    firing = False
    while lv1:
        bulletTxt = fnt.render(f'Bullet : {bullet}', False, 'white')
        SCREEN.blit(lvBkg, (20, 0))
        SCREEN.blit(lifeTxt, (20, 100))
        SCREEN.blit(scoreTxt, (20, 200))
        SCREEN.blit(bulletTxt, (20, 300))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == K_UP:
                    Player.y = Player.y - 30
                    print(playerStartPosY)
                if e.key == K_DOWN:
                    Player.y = Player.y + 50 
                if e.key == K_LEFT:
                    Player.x = Player.x - 50 
                if e.key == K_RIGHT:
                    Player.x = Player.x + 50 
                if e.key == K_SPACE:
                    firing = True
                    bullet_list.append([Player.x, Player.y])
                    bullet -= 1
        for bullet_pos in bullet_list[:]:
            bullet_pos[1] -= 5
            bullet_pos[0] += 0
        if Y == 0:
            bullet_list.remove(bullet_pos)
        for bullet_pos in bullet_list[:]:
            SCREEN.blit(bulletImg, bullet_pos)
        Player.update(SCREEN)
        clock.tick(60)
        pygame.display.update()
#runTime
intro()
Lv1()

 
     