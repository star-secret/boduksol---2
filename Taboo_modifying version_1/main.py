import convert_png as cp
import split_area as sa
import make_sensor as ma
import save_png as sp
import split_coordinate as sc
import random as rd
import move_sensor as ms
import judge_sensor as js
import copy

area_of_interest = []  #관심영역 좌표 list
sensor_list_xy = []  #xy sensor list

#입력(관심영역 & 센서 탐지거리)
sc.split_coord1(input("관심영역의 좌표를 입력하시오.").split(' '), area_of_interest) #입력 예시 (a,b) (b,c) (d,e)
detect_range = int(input("센서의 탐지범위를 입력하시오.")) #센서 탐지 거리
basic_png = sp.start(area_of_interest, [], detect_range)
basic_png.save_png()
total_pixel_of_interest = cp.convert_return_count("image_test0.png")
