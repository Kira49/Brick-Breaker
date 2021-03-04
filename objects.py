import global_var
import global_funct
import config
from headers import *
import logging
from time import time
class Object():

    def __init__(self, character, x, y):
        self.px, self.py = (x, y)
        self._width, self._height = (len(character[0]) ,len(character))
        self._shape, self.buff = (character, 0)

    def render(self):
        lis = [i for i in range (self.py, self._width+self.py)]
        lis2 = [i for i in range (self.px, self._height+self.px)]
        for i in lis:
            for j in lis2:
                global_var.mp.matrix[j][i] = self._shape[j-self.px][i-self.py]

    def get_c(self, axis):
        if axis == 0:
            return self.px
        return self.py

    def set_d(self, var, axis):
        if axis == 0:
            self.px = var
        else:
            self.py = var

    def set_c(self, var, axis):
        if axis == 0:
            self.px += var
        else:
            self.py += var

    def clear(self):
        lis = [i for i in range (0, self._width)]
        lis2 = [i for i in range (0, self._height)]
        for i in lis:
            for j in lis2:
                global_var.mp.matrix[j+self.py][i+self.px ] = ' '


class Paddle(Object):
    def __init__(self, character ,x, y, lives):
        super().__init__(character, x, y)
        self.__lives, self.__coins, self.__score = (3, 0, 0)
        self._width=len(character[0])

    def render(self):
        lis = [i for i in range (self.px, self._width+self.px)]
        lis2 = [i for i in range (self.py, self._height+self.py)]
        for i in lis:
            for j in lis2:
                global_var.mp.matrix[j][i] = self._shape[j-self.py][i-self.px]

class Ball(Object):

    def __init__(self, character ,x, y):
        super().__init__(character, x, y)
        self.check_collision2, self.check_ball2 = (0,0)

    def initial_movement(self):
        if self.check_collision2 == 0:
            self.px= global_var.paddle.get_c(0)+4

    def move_ball(self):
        if(self.get_c(0) >= 97):
            config.Ball_velocityx = -1*config.Ball_velocityx
            config.Ball_velocityx1 = -1*config.Ball_velocityx1
        elif(self.get_c(1) <= 6):
            config.Ball_velocityy = -1*config.Ball_velocityy
            config.Ball_velocityy1 = -1*config.Ball_velocityy1
        elif(self.get_c(1) == config.rows-1 and config.Ball_velocityy > 0):
            self.px , self.py = (global_var.paddle.px, global_var.paddle.py-2)
            config.check=0
            config.lives = config.lives - 1
            config.thru_flag1, config.thru_flag = (0, 0)
            config.is_expanded, config.is_expanded1 = (0, 0)
            if(config.is_shrunk==1 or config.is_shrunk1==0):
                config.is_shrunk, config.is_shrunk1, config.is_shrunk, config.is_shrunk1 = (0, 0, 0, 0)
                global_var.paddle._shape, global_var.paddle._width = (config.paddle1, 10)

            config.PaddleGrabflag, config.PaddleGrabflag1 = (0, 0)
            global_var.paddle_grab.stop_pow()

        elif(self.get_c(0) <= 1):
            config.Ball_velocityx = -1*config.Ball_velocityx
            config.Ball_velocityx1 =-1*config.Ball_velocityx1
            # self.px=global_var.paddle.px

        if(self.check_ball2!=1):
            self.set_c(config.Ball_velocityx, 0)
            self.set_c(config.Ball_velocityy, 1)
        else:
            self.set_c(config.Ball_velocityx1, 0)
            self.set_c(config.Ball_velocityy1, 1)

    def cleared(self):
        i, j = (self.py, self.px)
        if(i < 40 and j < 100 and global_var.mp.matrix[i][j]=='*'):
            global_var.mp.matrix[i][j] = ' '

    def render(self):
        global_var.mp.matrix[self.py][self.px] = '*'

    def check_collision(self):
        if(self.get_c(1)==global_var.paddle.py and config.Ball_velocityy>0):
            for i in range (0,global_var.paddle._width):
                j = 0
                if(i==0 or i==global_var.paddle._width -1 ):
                    j=1

                if(self.get_c(0) ==global_var.paddle.get_c(0)+i):

                    if(config.PaddleGrabflag==1):
                        # config.Ball_velocityy=0
                        # config.Ball_velocityx=0
                            # config.PaddleGrabflag1=1
                        self.px, self.py = (global_var.paddle.get_c(0)+4, global_var.paddle.get_c(1)-1)
                        config.check, config.PaddleGrabflag = (0, 0)

                    if(i==0):
                        config.Ball_velocityx = config.Ball_velocityx - j
                        config.Ball_velocityy = -1*config.Ball_velocityy

                    elif(i==global_var.paddle._width -1):
                        config.Ball_velocityx = config.Ball_velocityx + j
                        config.Ball_velocityy = -1*config.Ball_velocityy

                    else:
                        config.Ball_velocityx = config.Ball_velocityy + j
                        config.Ball_velocityy = -1*config.Ball_velocityy



class Power():
    def __init__(self, character ,x, y):
        self.px, self.py = (x, y)
        self._width, self._height = (len(character[0]),len(character))
        self._shape, self.FLAG= (character, 0)
        self.velocity, self.samay, self.check = (1, 0, 0)

    def get_c(self, axis):
        if axis == 0:
            return self.px
        else:
            return self.py

    def render(self):
        lis = [i for i in range (self.px, self._width+self.px)]
        lis2 = [i for i in range (self.py, self._height+self.py)]

        for i in lis:
            for j in lis2:
                global_var.mp.matrix[j][i] = self._shape[j-self.py][i-self.px]

    def move_powerup(self):

        if(self.get_c(1)==global_var.paddle.get_c(1) and self.get_c(0)>=global_var.paddle.get_c(0) and self.get_c(0)<=global_var.paddle.get_c(0)+global_var.paddle._width and self.check==0):
                self.FLAG, self.samay=(1, time())
                self.velocity, self.check = (0, 1)
                self._shape = " "

        if(self.get_c(1)!=global_var.later_ref+1):
            self.set_c(self.velocity, 1)
            return 0

    def clear(self):
        lis = [i for i in range (0, self._width)]
        lis2 = [i for i in range (0, self._height)]

        for i in lis:
            for j in lis2:
                global_var.mp.matrix[j+self.py][i+self.px ] = " "

    def set_c(self, var, axis):
        if axis == 0:
            self.px = self.px + var
        else:
            self.py = self.py + var

class thruball(Power):
    def __init__ (self,character,x,y):
        logging.info('here')
        super().__init__(character,x, y)
        self.thru1 = 0

    def start_pow(self):
        if(self.FLAG!=0):
            self.thru1 = 1
            config.thru_flag=1

    def stop_pow(self):

        if(round(time())-self.samay > 9) and self.FLAG!=0:
            config.thru_flag, config.thru_flag1 = (0, 0)
            self.FLAG=0


class expand(Power):
    def __init__ (self,character,x,y):
        logging.info('here')
        super().__init__(character,x, y)
        self.expand = 0

    def start_pow(self):
        if(self.FLAG!=0):
            global_var.paddle._shape, global_var.paddle._width = (config.paddle2, 12)
            config.is_expanded = self.FLAG

    def stop_pow(self):
        if(round(time())-self.samay > 9) and self.FLAG!=0:
            config.is_expanded, config.is_expanded1 = (0, 0)
            self.FLAG=0
            global_var.paddle._shape, global_var.paddle._width = (config.paddle1, 10)

class shrink(Power):
    def __init__ (self,character,x,y):
        logging.info('here')
        super().__init__(character,x, y)

    def start_pow(self):
        if(self.FLAG!=0):
            global_var.paddle._shape, global_var.paddle._width = (config.paddle3, 5)
            config.is_shrunk = self.FLAG

    def stop_pow(self):
        if(round(time())-self.samay > 4 and self.FLAG!=0):

            config.is_shrunk, config.is_shrunk1 = (0, 0)
            global_var.paddle._shape, global_var.paddle._width = (config.paddle1, 10)
            self.FLAG -= 1

class multiplier(Power):
    def __init__ (self,character,x,y):
        logging.info('here')
        super().__init__(character,x, y)

    def start_pow(self):
        if(self.FLAG!=0):
            config.multiplier_flag = self.FLAG


class fastball(Power):
    def __init__ (self,character,x,y):
        logging.info('here')
        super().__init__(character,x, y)
        self.check1=0
    def start_pow(self):
        if(self.FLAG!=0):
            if (config.Ball_velocityx<0 and self.check1!=1):
                config.Ball_velocityx = config.Ball_velocityx - 1
                self.check1=1

            elif(config.Ball_velocityx>=0 and self.check1!=1):
                config.Ball_velocityx = config.Ball_velocityx + 1
                self.check1 += 1


    def stop_pow(self):
        if(round(time())-self.samay >= 10) and self.FLAG==1:
            self.FLAG, config.fast_flag = (0, 0)
            if (config.Ball_velocityx<0):
                config.Ball_velocityx = config.Ball_velocityx + 1
            else:
                config.Ball_velocityx = config.Ball_velocityx - 1

class grab(Power):
    def __init__ (self,character,x,y):
        logging.info('here')
        super().__init__(character,x, y)

    def start_pow(self):
        if(self.FLAG==1):
            config.PaddleGrabflag = self.FLAG

    def stop_pow(self):
        if(round(time())-self.samay >= 10) and self.FLAG==1:
            config.PaddleGrabflag, config.PaddleGrabflag1 = (0, 0)
            self.FLAG=0
red = Fore.RED+ Back.RED
blue = Fore.BLUE+ Back.BLUE
green = Fore.GREEN+ Back.GREEN
white = Fore.WHITE + Back.WHITE
magenta = Fore.MAGENTA + Back.MAGENTA
class Brick():
    def __init__(self,x,y):
        self._height, self._width = (1, 9)

        self.shape= [['$' for i in range(10)]]
        self.px, self.py = (x, y)
        self.isthere = 0

    def clear(self):
        lis = [i for i in range (0, self._width)]
        lis2 = [i for i in range (0, self._height)]

        for i in lis:
            for j in lis2:
                global_var.mp.matrix[j+self.py][i+self.px ] = " "


    def render(self):
        lis = [i for i in range (0, self._width)]
        lis2 = [i for i in range (0, self._height)]

        if(self.isthere!=1):
            for i in lis:
                for j in lis2:
                    if(self.strength!=0):
                        if(self.strength-3==0):
                            global_var.mp.matrix[j+self.py][i+self.px] = red + self.shape[j][i]
                        if(self.strength-2==0):
                            global_var.mp.matrix[j+self.py][i+self.px] = blue + self.shape[j][i]
                        if(self.strength-1==0):
                            global_var.mp.matrix[j+self.py][i+self.px] = green + self.shape[j][i]
                        if(self.strength > 3):
                            global_var.mp.matrix[j+self.py][i+self.px] = white + self.shape[j][i]


    def check_collision_brick(self):
        lis = [i for i in range (0, self._width)]
        lis2 = [i for i in range (0, self._height)]

        for i in lis:
            for j in lis2:
                if i + self.px==global_var.ball.get_c(0) + config.Ball_velocityx and self.py==global_var.ball.get_c(1)+ config.Ball_velocityy and self.isthere==0:

                    if(config.thru_flag==1):
                        self.strength, self.isthere = (0,1)
                        config.score = config.score + 1
                        for i in range(0, self._width):
                            for j in range(0, self._height):
                                global_var.mp.matrix[j+self.py][i+self.px ] = ' '

                    else:
                        config.Ball_velocityy = -1*config.Ball_velocityy
                        self.strength = self.strength - 1
                        if(self.strength==0):
                            self.isthere = 1
                            config.score = config.score + 1
                            for i in lis2:
                                for j in lis:
                                    global_var.mp.matrix[i+self.py][j+self.px ] = ' '
                            if self.py == 6:
                                if(self.px<=global_var.a and self.px+self._width>=global_var.a + 1):
                                    config.thru_flag1 = self.isthere

                                if(self.px<=global_var.b and self.px+self._width>=global_var.b +1):
                                    config.is_expanded1= self.isthere
                            elif self.py == 16:
                                if(self.px<=global_var.c and self.px+self._width>=global_var.c + 1):
                                    config.is_shrunk1= self.isthere

                                if(self.px<=global_var.d and self.px+self._width>=global_var.d + 1):
                                    config.fast_flag= self.isthere

                                if(self.px<=global_var.e and self.px+self._width>=global_var.e + 1):
                                    config.PaddleGrabflag1= self.isthere



class Red_Bricks(Brick):
    def __init__ (self,x,y):
        super().__init__(x, y)
        self.color, self.strength = (red, 3)


class Blue_Bricks(Brick):
    def __init__ (self,x,y):
        super().__init__(x, y)
        self.color, self.strength = (blue, 2)


class Green_Bricks(Brick):
    def __init__ (self,x,y):
        super().__init__(x, y)
        self.color, self.strength = (green, 1)


class Gray_Bricks(Brick):
    def __init__ (self,x,y):
        super().__init__(x, y)
        self.color, self.strength = (white, 1000)

class Magenta_Bricks(Brick):
    def __init__ (self,x,y):
        logging.info('here')
        super().__init__(x, y)
        self.color = magenta
        self.strength = 1

    def render(self):
        lis = [i for i in range (self.px, self._width + self.px)]
        lis2 = [i for i in range (self.py, self._height + self.py)]

        if(self.isthere==0):
            for i in lis:
                for j in lis2:
                    global_var.mp.matrix[j][i] = self.color + self.shape[j-self.py][i-self.px]

    def check_collision_brick(self):
        lis = [i for i in range (0, self._width)]
        lis2 = [i for i in range (0, self._height)]

        for i in lis:
            for j in lis2:
                if i + self.px==global_var.ball.get_c(0) +  config.Ball_velocityx and self.py==global_var.ball.get_c(1)+config.Ball_velocityy and self.isthere==0:
                    if(config.thru_flag==1):
                        self.strength, config.blastflag = (0, 1)
                        config.blasty=self.py
                        if(self.strength==0):
                            self.isthere=1
                            for i in lis:
                                for j in lis2:
                                    global_var.mp.matrix[j+self.py][i+self.px ] = ' '

                    else:
                        config.Ball_velocityy = -1*config.Ball_velocityy
                        self.strength = self.strength -1
                        config.blastflag, config.blasty = (1, self.py)
                        if(self.strength==0):
                            self.isthere=1
                            for i in lis:
                                for j in lis2:
                                    global_var.mp.matrix[j+self.py][i+self.px ] = ' '
