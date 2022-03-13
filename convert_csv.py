import itertools
import numpy as np
import math
def con(ret_x,ret_y,ret_w,ret_h,router_point,room_pass_mat):
    print("entered")
    x_coords = [x for x in range(ret_x,ret_x+ret_w  + 1,10)]#[2,3,3,2,1,,1,1,1,2,2,2,]
    y_coords = [y for y in range(ret_y, ret_y+ret_h + 1,15)]#[2,2,,2,2,1,1,,1,2,2,2,]
    lst = list(itertools.product(x_coords, y_coords))
    output=[]
    for ele in lst:
        ele = ele + (round(math.sqrt(((ele[0]-router_point[0])**2)+((ele[1]-router_point[1])**2))),
        room_pass_mat[0],room_pass_mat[1],room_pass_mat[2],room_pass_mat[3],room_pass_mat[4],room_pass_mat[5],((round(math.sqrt(((ele[0]-router_point[0])**2)+((ele[1]-router_point[1])**2)))*0.42/12)+room_pass_mat[0])) ##[480,300500,0,0,0,0,0,0]
        output.append(ele)
    print(output)
    return(output)
#con(480,300,120,120,(0,0),"WC")
#   CONCRETE,        HBLOCK,           BRICK,          WOOD,              GLASS,           RCCROOF
#room_pass_mat[0],room_pass_mat[1],room_pass_mat[2],room_pass_mat[3],room_pass_mat[4],room_pass_mat[5],
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]
#[480,300500,0,0,0,0,0,0]