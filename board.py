from headers import *

class Screen(object):

    height, width = (int(config.rows), int(config.columns))

    def __init__(self):
        self.matrix = [[" " for i in range(0, self.width)] for j in range(0, self.height)]

        self.id_start = 0
        self.create_wall()
        self.create_cover(1)
        self.create_cover(0)


    def render(self):
        lis = [i for i in range(2, self.height-1)]
        tp = []
        abc = ""
        for x in range(self.id_start + config.columns):
            tp.append(Fore.LIGHTCYAN_EX + Style.BRIGHT+(self.matrix[3][x] + Style.RESET_ALL))
        abc = ("".join(tp))
        print(abc)
        for y in lis:
            pr = []
            for x in range(self.id_start + config.columns):
                abc = ""
                pr.append(self.matrix[y][x] + Style.RESET_ALL)
            abc=("".join(pr))
            print(abc)
        abc = ""
        tp2 = []
        for x in range(self.id_start + config.columns):
            tp2.append(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+(self.matrix[self.height-1][x] + Style.RESET_ALL))
        abc = ("".join(tp))
        print(abc)

    def create_wall(self):
        for y in range(0, self.height):
            self.matrix[y][0] = self.matrix[y][self.width-1] = "X"
            #  = "X"
    def create_cover(self, reg):
        y = 3
        var = "X"
        if reg == 0:
            y = self.height - 1
            var = "T"
        for x in range(0, self.width):
            self.matrix[y][x] = var
