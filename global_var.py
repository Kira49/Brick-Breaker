import board
import objects
import config
from headers import *
import os
from time import time
mp = board.Screen()


paddle = objects.Paddle(config.paddle, 5, mp.height - len(config.paddle)-2, config.lives)
time1= round(time())

a, b, c, d, e = (10, 20, 55, 65, 75)
Thru_Ball=objects.thruball(config.ThruBall_pow,a,6)
exp_paddle=objects.expand(config.ExpandPaddle_pow,b,6)
shrink_paddle=objects.shrink(config.ShrinkPaddle_pow,c,16)
fast_ball=objects.fastball(config.FastBall_pow,d,16)
paddle_grab=objects.grab(config.GrabBall_pow,e,16)

ball = objects.Ball(config.ball, paddle.get_c(0) + 4, paddle.get_c(1)-1)



later_ref = mp.height - len(config.paddle) - 1
j1, j2, j3, j4, j5, j6 = (5, 23, 10, 5, 20, 10)
red_Bricks=[]
for i in range(9):
    brck=objects.Red_Bricks(j1,6)
    j1 = j1 + 10
    red_Bricks.append(brck)
magenta_Bricks=[]
for i in range(6):
    brck=objects.Magenta_Bricks(j2,9)
    j2 = j2 + 10
    magenta_Bricks.append(brck)

blue_Bricks=[]
for i in range(8):
    brck=objects.Blue_Bricks(j3,8)
    j3 = j3 + 10
    blue_Bricks.append(brck)

green_Bricks=[]
for i in range(9):
    brck=objects.Green_Bricks(j4,10)
    j4 = j4 + 10
    green_Bricks.append(brck)

gray_Bricks=[]
for i in range(6):
    brck=objects.Gray_Bricks(j5,13)
    j5 = j5 + 10
    gray_Bricks.append(brck)

for i in range(9):
    brck=objects.Green_Bricks(j6,16)
    j6 = j6 + 10
    green_Bricks.append(brck)

def clearblast():
    if(config.blastflag==1):

        for i in range (9):
            if(red_Bricks[i].py==config.blasty+1 or red_Bricks[i].py==config.blasty-1 ):
                red_Bricks[i].strength, red_Bricks[i].isthere = (0, 1)
                red_Bricks[i].clear()

        for i in range (8):
            if(blue_Bricks[i].py==config.blasty+1 or blue_Bricks[i].py==config.blasty-1 ):
                blue_Bricks[i].strength, blue_Bricks[i].isthere = (0, 1)
                blue_Bricks[i].clear()

        for i in range (17):
            if(green_Bricks[i].py==config.blasty+1 or green_Bricks[i].py==config.blasty-1 ):
                green_Bricks[i].strength, green_Bricks[i].isthere = (0, 1)
                green_Bricks[i].clear()

        for i in range (6):
            if(gray_Bricks[i].py==config.blasty+1 or gray_Bricks[i].py==config.blasty-1 ):
                gray_Bricks[i].strength, gray_Bricks[i].isthere = (0, 1)
                gray_Bricks[i].clear()

        for i in range (6):
            if(magenta_Bricks[i].py==config.blasty ):
                magenta_Bricks[i].strength, magenta_Bricks[i].isthere = (0, 1)
                magenta_Bricks[i].clear()

def powerup(obj):
    obj.clear()
    obj.move_powerup()
    obj.start_pow()
    obj.stop_pow()
    obj.render()


def callthru_ball():
    powerup(Thru_Ball)

def callexpand():
    powerup(exp_paddle)

def callshrink():
    powerup(shrink_paddle)

def callfastball():
    powerup(fast_ball)

def callpaddlegrab():
    powerup(paddle_grab)
