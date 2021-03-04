import global_var
from headers import *
from time import time
import os
def create_header():
    print('\033[2;1H' + Fore.WHITE + Back.BLUE + Style.BRIGHT + 
    ('SCORE: ' + str(config.score) + '   |  LIVES: ' + str(config.lives) + '   |  TIME: ' + str(round(time())-global_var.time1)).center(config.columns))
    print(Style.RESET_ALL)

def print_board():
    create_header()
    global_var.paddle.render()
    global_var.mp.render()
