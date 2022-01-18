import pygame, sys

from pygame.locals import *

import random

pygame.init()

over=False

collision=False

SNAKEX=[]

SNAKEY=[]

score=0

cornerx=0

cornery=0

DISPLAYSURF=pygame.display.set_mode((500,500))

def initSnake():
    x=random.randint(0,9)
    y=random.randint(0,9)
    SNAKEX.append(x*50)
    SNAKEY.append(y*50)
    if(SNAKEX[0]==cornerx and SNAKEY[0]==cornery):
        pygame.draw.rect(DISPLAYSURF,(255,255,0),(SNAKEY[0],SNAKEX[0],50,50))
    else:
        pygame.draw.rect(DISPLAYSURF,(0,255,0),(SNAKEX[0],SNAKEY[0],50,50))

def  up():
    global collision
    if(collision==False):
        frontY=SNAKEY[0]-50
        frontX=SNAKEX[0]
        SNAKEX.insert(0,frontX)
        SNAKEY.insert(0,frontY)
        SNAKEX.pop()
        SNAKEY.pop()
    else:
        frontY=SNAKEY[0]-50
        frontX=SNAKEX[0]
        SNAKEX.insert(0,frontX)
        SNAKEY.insert(0,frontY)
        collision=False
    
def down():
    global collision
    if(collision==False):
        frontY=SNAKEY[0]+50
        frontX=SNAKEX[0]
        SNAKEX.insert(0,frontX)
        SNAKEY.insert(0,frontY)
        SNAKEX.pop()
        SNAKEY.pop()
    
    else:
        frontY=SNAKEY[0]+50
        frontX=SNAKEX[0]
        SNAKEX.insert(0,frontX)
        SNAKEY.insert(0,frontY)
        collision=False


def left():
    global collision
    if(collision==False):
        frontX=SNAKEX[0]-50
        frontY=SNAKEY[0]
        SNAKEX.insert(0,frontX)
        SNAKEY.insert(0,frontY)
        SNAKEX.pop()
        SNAKEY.pop()
    else:
        frontX=SNAKEX[0]-50
        frontY=SNAKEY[0]
        SNAKEX.insert(0,frontX)
        SNAKEY.insert(0,frontY)
        collision=False




def right():
    global collision
    if(collision==False):
        frontX=SNAKEX[0]+50
        frontY=SNAKEY[0]
        SNAKEX.insert(0,frontX)
        SNAKEY.insert(0,frontY)
        SNAKEX.pop()
        SNAKEY.pop()
    else:
        frontX=SNAKEX[0]+50
        frontY=SNAKEY[0]
        SNAKEX.insert(0,frontX)
        SNAKEY.insert(0,frontY)
        collision=False


def drawSnake():
    for i in range(len(SNAKEX)):
        pygame.draw.rect(DISPLAYSURF,(255,255,0),(SNAKEX[i],SNAKEY[i],50,50))


def point():
    global cornerx, cornery
    x=random.randint(0,9)
    y=random.randint(0,9)
    cornerx=x*50
    cornery=y*50
    pygame.draw.rect(DISPLAYSURF,(0,255,0),(cornerx,cornery,50,50))

def grid():
    x=0
    y=0
    for i in range(9):
        x+=50
        y+=50
        pygame.draw.line(DISPLAYSURF,(255,255,255),(x,0),(x,500))
        pygame.draw.line(DISPLAYSURF,(255,255,255),(0,y),(500,y))

def gameOver():
    global over,SNAKEX,SNAKEY
    over=True
    fontObj=pygame.font.Font("freesansbold.ttf",64)
    fontSurf=fontObj.render("GAME OVER",True,(255,255,255))
    fontRect=fontSurf.get_rect()
    fontRect.center=(250,250)
    DISPLAYSURF.blit(fontSurf,fontRect)
    fontObj=pygame.font.Font("freesansbold.ttf",32)
    fontSurf=fontObj.render("Press Enter to Restart",True,(255,255,255))
    fontRect=fontSurf.get_rect()
    fontRect.center=(250,320)
    DISPLAYSURF.blit(fontSurf,fontRect)
    SNAKEX=[]
    SNAKEY=[]

point()

initSnake()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_UP:
                up()
            if event.key==K_DOWN:
                down()
            if event.key==K_LEFT:
                left()
            if event.key==K_RIGHT:
                right()
            if event.key==K_RETURN:
                if over==True:
                    score=0
                    initSnake()
                    over=False
    if over==False:
        if(cornerx==SNAKEX[0] and cornery==SNAKEY[0]):
            score+=1
            collision=True
            point()

    if(over==False):
        for i in range(len(SNAKEX)):
            for j in range(len(SNAKEX)):
                if(i!=j):
                    if((SNAKEX[i]==SNAKEX[j] and SNAKEY[i]==SNAKEY[j])): 
                        gameOver()
                        break
    
    if(over==False):
        if(SNAKEX[0]<0 or SNAKEX[0]>450 or SNAKEY[0]<0 or SNAKEY[0]>450):
            gameOver()
    pygame.display.set_caption(f"Snake Score : {score}")
    DISPLAYSURF.fill((0,0,0))
    grid()
    pygame.draw.rect(DISPLAYSURF,(0,255,0),(cornerx,cornery,50,50))
    if(over==True):
        gameOver()
    if(over==False):
        drawSnake()
    pygame.display.update()