import math

def is_point_inside(opst_corner1, opst_corner2, point):
    if (point[0] > opst_corner1[0] and point[0] < opst_corner2[0] and point[1] > opst_corner1[1] and point[1] < opst_corner2[1]):
        return True
    else:
        return False


def line_passing_through_two_point(co1,co2):
    a = co2[1]-co1[1]
    b = co1[0]-co2[0]
    c = -(a*(co1[0]) + b*(co1[1]))
    return {
        "x_coef": a,
        "y_coef": b,
        "const": c
    }

def opposit_corner_of_rectangle(rectangle_cords):
    opp_cor = []
    return [item for item in rectangle_cords if item[1] not in opp_cor and not opp_cor.append(item[1])]


def distance_between_line_and_point(x_coef, y_coef, const, x, y):
    dist = ((abs(x_coef*x + y_coef*y + const))/math.sqrt(x_coef**2 + y_coef**2))
    return dist

def coordinate_after_rotation(origin, point, angle):
    angle = math.radians(angle)
    x_cord = origin[0] + math.cos(angle) * (point[0] - origin[0]) - math.sin(angle) * (point[1] - origin[1])
    y_cord = origin[1] + math.sin(angle) * (point[0] - origin[0]) + math.cos(angle) * (point[1] - origin[1])
    return (x_cord, y_cord)


def get_angle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def centroid(point_lst):
    p1 = point_lst[0]
    p2 = point_lst[1]
    p3 = point_lst[2]
    p4 = point_lst[3]

    x_cor = (p1[0]+p2[0]+p3[0]+p4[0])/4
    y_cor = (p1[1]+p2[1]+p3[1]+p4[1])/4
    return (x_cor, y_cor)