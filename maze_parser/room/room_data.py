class room_data:
    def __init__(self):
        self.__edges = [0 for _ in range(4)]
    def get_edges(self):
        return self.__edges
    def set_edges(self, edges):
        self.__edges = edges
    def turn_off_up(self):
        self.__edges[0] = 0;
    def turn_off_right(self):
        self.__edges[1] = 0;
    def turn_off_down(self):
        self.__edges[2] = 0;
    def turn_off_left(self):
        self.__edges[3] = 0;
    def turn_up_parent(self):
        self.__edges[0] = 2;
    def turn_right_parent(self):
        self.__edges[1] = 2;
    def turn_down_parent(self):
        self.__edges[2] = 2;
    def turn_left_parent(self):
        self.__edges[3] = 2;
    def turn_up_child(self):
        self.__edges[0] = 1;
    def turn_right_child(self):
        self.__edges[1] = 1;
    def turn_down_child(self):
        self.__edges[2] = 1;
    def turn_left_child(self):
        self.__edges[3] = 1;
    def edges_off(self):
        for i in range(4):
            if self.__edges[i] != 0:
                return 0
        return 1
