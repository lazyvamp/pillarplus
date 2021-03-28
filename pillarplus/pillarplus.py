import math
from common_utils import *
from itertools import combinations

#question1

list_co = [
    [4558.1082569293285,6225.585248947349,0],
    [3957.525350060251,6225.585248947349,0],
    [3957.525350060251,6654.395984582226,0],
    [4558.1082569293285,6654.395984582226,0]
]

def edge(co1,co2):
    x = math.pow((co1[0]-co2[0]),2)
    y = math.pow((co1[1]-co2[1]),2)
    z = math.pow((co1[2]-co2[2]),2)
    len = math.sqrt(x+y+z)
    return len

def edge_finder(list_co):
    right_edge = edge(list_co[0],list_co[1])
    left_edge = edge(list_co[1],list_co[2])
    bottom_edge = edge(list_co[2],list_co[3])
    top_edge = edge(list_co[3],list_co[0])
    return (
        print(
            "Right Edge: {}""  Left Edge: {}""  Top Edge: {}""  Bottom Edge: {}".format(right_edge, left_edge, top_edge,bottom_edge) 
        )
    )

edge_finder(list_co)

print("=======================")

#question2

matrix = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,0,0],
    [1,0,0,0]
]

mat2 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]


def component_finder(mat):
    position_list = []
    final_list = []
    for x in range(0,4):
        for y in range(0,4):
            if mat[x][y]==1:
                if mat[x][y] not in position_list:
                    position_list.append((x,y))
    #list of coordinate having 1 val at it
    for point in position_list:
        for x in range(-1,2):
            for y in range(-1,2):
                if 0<=(point[0]-x):
                    if 0<=(point[1]-y):
                        if point != ((point[0]-x),(point[1]-y)):
                            try:
                                val = mat[(point[0]-x)][(point[1]-y)]
                                if val == 1:
                                    final_list.append((point, ((point[0]-x),(point[1]-y))))
                            except:
                                pass
    #list of pairs of coordinate / component
    print("components are:",final_list)
component_finder(matrix)

print("=======================")
#question3

rectangle_cords = [(0,0),(10,0),(10,10),(0,10)]
circles_loc = {(5,5):1,(11,9):2,(12,12):1,(9,9):2} 
    
def circle_perfectly_lie_inside_rectangle(rectangle_cords, circles_loc):
    line_data = []
    for i in range(0,4):
        if i<3:
            l = line_passing_through_two_point(rectangle_cords[i], rectangle_cords[i+1])
        else:
            l = line_passing_through_two_point(rectangle_cords[i], rectangle_cords[i-3])
        line_data.append(l)
    distance_from_lines = []
    circles_loc_keys = []
    for n in circles_loc.keys():
        distences = []
        circles_loc_keys.append(n)
        for m in line_data:
            d = distance_between_line_and_point(m['x_coef'],m['y_coef'],m['const'],n[0],n[1])
            distences.append(d)
        distance_from_lines.append(distences)
    answer = {}
    opp_cor = opposit_corner_of_rectangle(rectangle_cords)
    for i in range(0,4):
        if is_point_inside(opp_cor[0], opp_cor[1], circles_loc_keys[i]) is True:
            if circles_loc[circles_loc_keys[i]] < distance_from_lines[i][0]:
                if circles_loc[circles_loc_keys[i]] < distance_from_lines[i][1]:
                    if circles_loc[circles_loc_keys[i]] < distance_from_lines[i][2]:
                        if circles_loc[circles_loc_keys[i]] < distance_from_lines[i][3]:
                            answer[circles_loc_keys[i]] = circles_loc[circles_loc_keys[i]]

    print("perfectly inside circles are:-" , answer)
circle_perfectly_lie_inside_rectangle(rectangle_cords, circles_loc)

print("=======================")

#Question4
#coordinate_after_rotation(origin=(0,0), point=(1,2), angle=180)
points = [(0,5),(0,0),(0,10),(5,10),(10,10),(0,7),(10,0),(10,3)]

def corners_of_rectangle(points):
    cord_map = {}
    for point in points:
        if point[0] not in cord_map.keys():
            cord_map[point[0]] = [point[1]]
        else:
            cord_map[point[0]].append(point[1])
    min_x = min(cord_map.keys())
    max_x = max(cord_map.keys())
    
    corner_1 = (min_x, min(cord_map[min_x]))
    corner_3 = (max_x, max(cord_map[max_x]))
    list_corner = [corner_3, corner_1]
    
    for point in points:
        angle = get_angle(corner_1, point, corner_3)
        if angle%90 == 0:
            if point not in list_corner:
                list_corner.append(point)
    centrd = centroid(list_corner)
    return list_corner, centrd

# l2 = [(0,0), (0.5,0.5), (1,1), (1.5, 0.5), (2,0), (1.5,-0.5), (1,-1), (0.5,-0.5)]
# test_lst = [(0,1), (1,0), (2,3), (3,2), (1,2), (2,1), (0.5,0.5), (2.5,2.5)]
corner_list, centroid_of_rect = corners_of_rectangle(points)

def rotated_coordinates(points, angle):
    corner_list, center = corners_of_rectangle(points)
    print("original coordinates of rectangle are:", corner_list)
    new_coordinates = []
    for i in range(0,4):
        cord = coordinate_after_rotation(center, corner_list[i], angle)
        new_coordinates.append(cord)
    return print("after rotation of {} new coordinates are: ".format(angle), new_coordinates)
rotated_coordinates(points, 45)

print("=======================")

#queston5
circles_loc = {(5,5):1,(11,9):2,(12,12):1,(9,9):2}

def circle_find(center):
    if circles_loc[center] == 2:
        return True
    else:
        return False

d = filter(circle_find, circles_loc)

print("circles with rdious 2 having center at", [x for x in d])