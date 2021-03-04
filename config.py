from headers import *

columns = 100
rows = 40
score=0
lives = 3
check=0
paddle1 = [['Y' for i in range(10)]]
paddle2 = [['Y' for i in range(13)]]
paddle3 = [['Y' for i in range(6)]]
# paddle_width=9
ball, ThruBall_pow, ExpandPaddle_pow, ShrinkPaddle_pow, FastBall_pow, BallMultiply_pow, GrabBall_pow = ([["*"]], [["T"]], [["E"]], [["S"]], [["F"]], [["M"]], [["G"]])
Ball_velocityx, Ball_velocityy, Ball_velocityx1, Ball_velocityy1 = (0, -1, 1, -1)
pow_velocity=1
thru_flag1, thru_flag, fast_flag, is_expanded, is_expanded1, multiplier_flag, multiplier_flag1, is_shrunk, is_shrunk1, blastflag = (0,)*10
blasty=-2
is_shrunk, checkii, PaddleGrabflag, PaddleGrabflag1 = (0,)*4

padding = ""

if(is_expanded!=0):
    paddle=paddle2
if(is_shrunk==1 and is_expanded==0):
    paddle=paddle3
if is_shrunk==0 and is_expanded==0:
    paddle=paddle1
