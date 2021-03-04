from input import *
from headers import *
import global_var
from global_var import paddle, ball
import global_funct
import objects
import config
if(__name__=="__main__"):
    Get_obj=Get()
    while(1):
        paddle.clear()
        inp = input_to(Get_obj)
        ball.check_collision()
        sys.stdout.write('\033c')
        if(inp!=None):
            sleep(0.049)

        if(inp =='q'):
            print('you quit')
            break

        elif inp == 'd':
            if paddle.get_c(0) <= global_var.mp.id_start + config.columns - 3 - paddle._width and paddle.get_c(0) <= 1090:
                paddle.set_c(4, 0)

        elif inp == 'a':
            if paddle.get_c(0) > global_var.mp.id_start + 1:
                paddle.set_c(-4, 0)


        if config.lives == 0:
            os.system('tput reset')
            print(('    _____                         ____                 ').center(config.columns))
            print(('   / ____|                       / __ \                ').center(config.columns))
            print(('  | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ').center(config.columns))
            print(('  | | |_ |/ _  |  _   _ \ / _ \ | |  | \ \ / / _ \  __|').center(config.columns))
            print(('  | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ').center(config.columns))
            print(('   \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ').center(config.columns))
            print(Style.RESET_ALL)
            print(Fore.CYAN + Style.BRIGHT + ('SCORE: ' + str(config.score)).center(config.columns))
            print(Style.RESET_ALL)
            print(Fore.CYAN + Style.BRIGHT + ('LIVES: ' + str(config.lives)).center(config.columns))
            print(Style.RESET_ALL)
            print(Fore.CYAN + Style.BRIGHT + ('TIME: ' + str(round(time())-global_var.time1)).center(config.columns))
            print(Style.RESET_ALL)
            break

        if(config.check==0):
            ball.render()
            ball.cleared()
            ball.initial_movement()
            ball.render()

        if(inp=='r' or config.check!=0):
            config.check=1
            ball.cleared()
            ball.move_ball()
            ball.cleared()
            ball.render()


        for i in range (9):
            global_var.red_Bricks[i].render()
            global_var.red_Bricks[i].check_collision_brick()

        for i in range (8):
            global_var.blue_Bricks[i].render()
            global_var.blue_Bricks[i].check_collision_brick()

        for i in range (17):
            global_var.green_Bricks[i].render()
            global_var.green_Bricks[i].check_collision_brick()

        for i in range (6):
            global_var.gray_Bricks[i].render()
            global_var.gray_Bricks[i].check_collision_brick()

        for i in range (6):
            global_var.magenta_Bricks[i].render()
            global_var.magenta_Bricks[i].check_collision_brick()

        if(config.thru_flag1!=0):
            global_var.callthru_ball()

        if(config.is_expanded1!=0):
            global_var.callexpand()

        if(config.is_shrunk1!=0):
            global_var.callshrink()

        if(config.fast_flag!=0):
            global_var.callfastball()

        if(config.PaddleGrabflag1!=0):
            global_var.callpaddlegrab()

        # if(config.multiplier_flag1==1):
        #     global_var.callmultiplier()

        global_var.clearblast()
        paddle.render()
        global_funct.print_board()
