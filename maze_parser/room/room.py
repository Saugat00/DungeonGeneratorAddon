from . import room_data

class Room:
    def __init__(self, *args, **kwargs):
        if  'room_data' in kwargs:
            self.__room_data = room_data
        elif 'init_data' in kwargs and kwargs.get('init_data') == True:
            self.__room_data = room_data()
        else:
            self.__room_data = None
        if 'left' in kwargs:
            self.__left = kwargs.get('left')
        else:
            self.__left = None
        if 'right' in kwargs:
            self.__right = kwargs.get('right')
        else:
            self.__right = None
        if 'down' in kwargs:
            self.__down = kwargs.get('down')
        else:
            self.__down = None
        if 'up' in kwargs:
            self.__up = kwargs.get('up')
        else:
            self.__up = None
        if 'x' in kwargs:
            self.__x = kwargs.get('x')
        else:
            self.__x = 0
        if 'y' in kwargs:
            self.__y = kwargs.get('y')
        else:
            self.__y = 0
    def get_right(self):
        return self.__right
    def set_right(self, right):
        self.__right = right
    def turn_off_right(self):
        self.__right = 0;
    def get_left(self):
        return self.__left
    def set_left(self, left):
        self.__left = left
    def get_up(self):
        return self.__up
    def set_up(self, up):
        self.__up = up
    def get_down(self):
        return self.__down
    def set_down(self, down):
        self.__down = down
    def get_room_data(self):
        return self.__room_data
    def set_room_data(self, room_data):
        self.__room_data = room_data
    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x
    def get_y(self):
        return self.__y
    def set_y(self, y):
        self.__y = y
    def init_block(self):
        return self.__room_data.edges_off()
