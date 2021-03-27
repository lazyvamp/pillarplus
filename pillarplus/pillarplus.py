import math
from common_utils import *
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
        if circles_loc[circles_loc_keys[i]] < distance_from_lines[i][0] and distance_from_lines[i][1] and distance_from_lines[i][2] and distance_from_lines[i][3]:
            if is_point_inside(opp_cor[0], opp_cor[1], circles_loc_keys[i]) is True: 
                answer[circles_loc_keys[i]] = circles_loc[circles_loc_keys[i]]

    print("perfectly inside circles are:-" , answer)
circle_perfectly_lie_inside_rectangle(rectangle_cords, circles_loc)


#queston5
circles_loc = {(5,5):1,(11,9):2,(12,12):1,(9,9):2} 

rds = []
keys = []
for c, r in circles_loc.items():
    rds.append(r)
    keys.append(c)

def circle_find(rad):
    if rad == 2:
        return True
    else:
        return False

d = filter(circle_find, rds)

count = 0
for c in d:
    count+=1

d=[k for k,v in circles_loc.items() if v == 2]
print("circles with rdious 2 are:", count, "and having center at", d)