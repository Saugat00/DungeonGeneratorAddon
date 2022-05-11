def tertiary_parse(parent, current):
    """ Parses a collection of vectors and returns object lang of physical model
    """
    if   parent == 1:
        if   current == 1:
            return "a"
        elif current == 2:
            return "d"
        elif current == 4:
            return "c"
        elif current == 10:
            return "u"
    elif parent == 2:
        if current == 1:
            return "f"
        elif current == 2:
            return "b"
        elif current == 3:
            return "c"
        elif current == 9:
            return "v"
    elif parent == 3:
        if current == 2:
            return "e"
        elif current == 3:
            return "a"
        elif current == 4:
            return "f"
        elif current == 10:
            return "s"
    elif parent == 4:
        if current == 1:
            return "e"
        elif current == 3:
            return "d"
        elif current == 4:
            return "b"
        elif current == 9:
            return "t"

def parse_path(P, h, w):
    M = [["0" for _ in range(w)] for _ in range(h)]
    first_tile(P, M, h, w)

    for i in range(1, len(P) - 1):
        M[P[i][1]][P[i][0]] = tertiary_parse(P[i - 1][2], P[i][2])

    last_tile(P, M, h, w)
    return M

def first_tile(P, M, h, w):
    if P[0][2] == 1:
        M[P[0][1]][P[0][0]] = "i"
    elif P[0][2] == 2:
        M[P[0][1]][P[0][0]] = "h"
    elif P[0][2] == 3:
        M[P[0][1]][P[0][0]] = "g"
    elif P[0][2] == 4:
        M[P[0][1]][P[0][0]] = "j"
    return M 

def last_tile(P, M, h, w):
    if P[len(P) - 1][2] == 5:
        M[P[len(P) - 1][1]][P[len(P) - 1][0]] = "g"
    elif P[len(P) - 1][2] == 6:
        M[P[len(P) - 1][1]][P[len(P) - 1][0]] = "j" 
    elif P[len(P) - 1][2] == 7:
        M[P[len(P) - 1][1]][P[len(P) - 1][0]] = "i"
    elif P[len(P) - 1][2] == 8:
        M[P[len(P) - 1][1]][P[len(P) - 1][0]] = "h"
