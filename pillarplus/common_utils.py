import math

def is_point_inside(opst_corner1, opst_corner2, point):
    if (point[0] > opst_corner1[0] and point[0] < opst_corner2[0] and point[1] > opst_corner1[1] and point[1] < opst_corner2[1]):
        return True
    else:
        return False


def line_passing_through_two_point(co1,co2):
    a = co2[1]-co1[1]
    b = co1[0]-co2[0]
    c = a*(co1[0]) + b*(co1[1])
    return {
        "x_coef": a,
        "y_coef": b,
        "const": c
    }

def opposit_corner_of_rectangle(rectangle_cords):
    opp_cor = []
    return [item for item in rectangle_cords if item[1] not in opp_cor and not opp_cor.append(item[1])]


def distance_between_line_and_point(x_coef, y_coef, const, x, y):
    dist = ((abs(x_coef * x + y_coef * y + const))/math.sqrt(x_coef ** 2 + y_coef ** 2))
    return dist

