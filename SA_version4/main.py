import convert_png as cp
import make_sensor as msp
import save_png as spm
import split_coordinate as sc
import move_coordinate as mc
import move_change
import random_move
import numpy as np
import copy
import judge_sensor as sl
from random import *
import math
import matplotlib.pyplot as plt



sensorxy = []
T_init = 60
T_final = 1
T = copy.deepcopy(T_init)
parameter = 10
#n=0.99 #반복횟수 약 400회
n=0.9 #반복횟수 약 100회
area_of_interest_list = []
sc.split_coord1(input("관심영역의 좌표를 입력하시오.").split(' '), area_of_interest_list) #관심영역 좌표 리스트
#입력 예시 (200,200) (600,200) (400,540)           // (286,39) (515,408) (58,410)
detect_range = int(input("센서의 탐지범위를 입력하시오.\n"))

length = 9#move의 숫자열 길이

sensor_number = 1
move = [] #예시=[[0,1,0,0,1,0,0,1,1],[1,0,0,1,0,0,1,0,1]]
tempmove = []
sensor = [] #예시=[[100,200],[200,300]]
tempsensor = []
count = 0
objportion = 0
portiongraph = [] #각 센서의 커버율을 list로 저장해 그래프로 나타낼것임

while objportion < 100:
    #관심영역의 총 픽셀 계산
    basic_png = spm.start(area_of_interest_list,[],detect_range)
    basic_png.save_png()
    total_pixel_of_interest = cp.convert_return_count("image_test0.png")


    ideal_portion = round(sensor_number*(detect_range ** 2)*math.pi/(total_pixel_of_interest/100),2)
    if ideal_portion > 100:
        ideal_portion = 100


    print("이상적인 커버율:")
    print(ideal_portion)
    print("센서 개수:",end="")
    print(sensor_number)

    for i in range(sensor_number):
        sensor.append(msp.area(area_of_interest_list).propercordinate())

    basic_png.change_sensor(sensor)
    basic_png.save_png()
    count+=1
    obj = cp.convert_return_count("image_test"+str(count)+".png")
    objportion = cp.convert_return_portion(obj,total_pixel_of_interest)

    for i in range(sensor_number):
        move.append([0,0,0,0,1,1,1,0,1])
        tempmove.append(random_move.create_move(length))

    print("initial portion:"+str(objportion))
    initial_portion=copy.deepcopy(objportion)

    while T>=T_final:
        tempsensor = copy.deepcopy(sensor)
        tempsensor = mc.move_coordinate(tempsensor,tempmove)

        for i in range(sensor_number):
            if sl.inner_discrimination(area_of_interest_list,tempsensor[i])==1:
                tempsensor[i]=copy.deepcopy(sensor[i])

        basic_png.change_sensor(tempsensor)
        basic_png.save_png()
        count+=1
        tempobj = cp.convert_return_count("image_test"+str(count)+".png")
        tempobjportion = cp.convert_return_portion(tempobj, total_pixel_of_interest)


        if np.exp((tempobjportion-objportion)/T*parameter)>=random():
            sensor = copy.deepcopy(tempsensor)
            move = copy.deepcopy(tempmove)
            fin_count=copy.deepcopy(count)
            obj = tempobj
            objportion = tempobjportion
            print(fin_count)

        if (objportion+0.1*sensor_number >= ideal_portion):  #픽셀계산의 오류에 따른 오차값 빼주기, 오차값은 추후 실험을 통해 정밀한 계산이 필요할 것으로 보임
            break

        tempmove = move_change.random_nextMove_change1(move)
        T=T*n

    obj = cp.convert_return_count("image_test"+str(fin_count)+".png")
    #print(obj)
    objportion = cp.convert_return_portion(obj, total_pixel_of_interest)
    print("final_portion :"+str(objportion))
    print("delta_portion : "+str(round(objportion-initial_portion,2)))

    sensor_number=sensor_number+1
    sensor.clear()#list 및 변수초기화해서 다음 센서개수로 넘어가는 부분
    move.clear()
    tempmove.clear()
    T=T_init
    portiongraph.append(objportion)

#그래프 그리는 부분
plt.plot(portiongraph)
plt.show()