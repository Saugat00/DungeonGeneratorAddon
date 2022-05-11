import random as rand

from .sorting_algorithm import sorting_algorithm
from .maze_parser import parse_path

class recursive_backtracing(sorting_algorithm):
    def __init__(self, *args, **kwargs):
        if 'h' in kwargs:
            self.h = kwargs.get('h')
        else:
            self.h = 10
        if 'w' in kwargs:
            self.w = kwargs.get('w')
        else:
            self.w = 10
        self.ix = 0
        self.iy = 0
        self.path = self.generate_dungeon()

    def generate_dungeon(self):
        P = [[0 for _ in range(self.w)] for _ in range(self.h)]
        rand.seed()                         # Start random module
        self.ix = rand.randrange(0, self.w) # Set Notation-> [0, (w - 1)]
        self.iy = rand.randrange(0, self.h) # Set Notation-> [0, (h - 1)]
        x_curr  = self.ix                   # start x at the x start
        y_curr  = self.iy                   # start y at the y start
        choice  = 0
        self.recursive_backtracing(P, self.ix, self.iy, x_curr, y_curr)
        print(P)
        return parse_path(P, self.h, self.w)

    def recursive_backtracing(self, P, x_s, y_s, x_c, y_c):
        P[y_c][x_c] = self.vacant_adjaccent_choice(P, x_c, y_c)
        if P[y_c][x_c] == 1 and y_c - 1 >= 0:
            y_c -= 1
        elif P[y_c][x_c] == 2 and x_c + 1 < self.w:
            x_c += 1
        elif P[y_c][x_c] == 3 and y_c + 1 < self.h:
            y_c += 1
        elif P[y_c][x_c] == 4 and x_c - 1 >= 0:
            x_c -= 1
        elif P[y_c][x_c] == 9:
            self.recursive_backtracing(P, x_s, y_s, x_c, y_c + 1)
            self.recursive_backtracing(P, x_s, y_s, x_c, y_c - 1)
            return
        elif P[y_c][x_c] == 10:
            self.recursive_backtracing(P, x_s, y_s, x_c + 1, y_c)
            self.recursive_backtracing(P, x_s, y_s, x_c - 1, y_c)
            return
        if (x_c != x_s and y_s != y_c):
            # Get a choice from vacant adjaccent neighbor vecotrs
            self.recursive_backtracing(P, x_s, y_s, x_c, y_c)

    def vacant_adjaccent_choice(self, P, x_c, y_c):
        i = self.get_neighbor(P, x_c, y_c)
        print(i)
        if i == -1:
            return 0
        else:
            return i

    def get_neighbor(self, P, x_c, y_c):
        A = []
        print('(', x_c, y_c, ')')
        if y_c + 1 < self.h and x_c < self.w and y_c + 1 >= 0 and x_c >= 0:
            if P[y_c + 1][x_c] != 0:
                A.append(P[y_c + 1][x_c])
        if x_c + 1 < self.w and y_c < self.h and y_c >= 0 and x_c + 1 >= 0:
            if P[y_c][x_c + 1] != 0:
                A.append(P[y_c][x_c + 1])
        if y_c - 1 >= 0 and x_c >= 0 and x_c < self.w and y_c - 1 < self.h:
            if P[y_c - 1][x_c] != 0:
                A.append(P[y_c - 1][x_c])
        if x_c - 1 >= 0 and y_c >= 0 and x_c - 1 < self.w and y_c < self.h:
            if P[y_c][x_c - 1] != 0:
                A.append(P[y_c][x_c - 1])
        if not (1 in A and 3 in A):
            A.append(9)
        if not (2 in A and 4 in A):
            A.append(10)
        print(A)
        if len(A) >= 1:
            return rand.choice(A)
        else:
            return -1
    def print_path(self):
        for i in range(len(self.path)):
            print(self.path[i])
