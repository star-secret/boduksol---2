import math, sys
import pygame
import time, random
from pygame.locals import *

#함수화..

polygon_list = []
polygon_list.append((10,10))
polygon_list.append((1200,10))
polygon_list.append((1200,700))
polygon_list.append((10,700))

polygon_list2 = []
polygon_list2.append([10,10])
polygon_list2.append([1200,10])
polygon_list2.append([1200,700])
print(polygon_list)
sensor_list=[]
sensor_list.append([100,200])
sensor_list.append([400,500])

sensor_list2=[]
sensor_list2.append([1200,700])
sensor_list2.append([700,600])

print(sensor_list)

radius= 30
class start:
    #관심영역리스트, 반지름1인 센서들의 중심좌표 리스트, 반지름2인 센서들의 중심좌표 리스트, 반지름1, 반지름2
    #만약에 반지름의 크기를 다르게하고 싶지 않으면 반지름 1이나 반지름2에다가 0을 집어넣으면 된다.
    def __init__(self,input_list,input_sensor1,input_sensor2,input_radius1,input_radius2):      #input_list는 이제 관심영역 리스트 입력받는거, input_sensor는 센서 중심좌표를 리스트로 받는것
                                                                    #input_radius는 센서의 반지름을 입력받는거
        self.screen_size= (1360,768)   
        self.polygon= [] + input_list  
        self.countpicture = 0           
        self.sensor1 = [] + input_sensor1 
        self.sensor2 = [] + input_sensor2
        self.sensor_radius1 = input_radius1
        self.sensor_radius2 = input_radius2
        self.countsensor = len(self.sensor1)+len(self.sensor2)  #센서 갯수 

    def runGame(self,screen):
        run=True
        while run:
            for event in pygame.event.get():
                if event.type == QUIT:
                    run=False
        
            pygame.draw.polygon(screen,(0,0,0),self.polygon)   #관심영역 그리기, screen에다가 (0,0,0)이니까 검정색으로, self.polygon이 관심영역의 꼭지점을 좌표로 받은거니이 꼭지점으로 다각형그리는거
            if self.sensor_radius1 != 0:
                for number in self.sensor1:            #센서의 중심좌표 개수만큼 센서 그려주는거임
                    pygame.draw.circle(screen,(180,160,100),number,self.sensor_radius1,0)
            if self.sensor_radius2 != 0:
                for number in self.sensor2:            #센서의 중심좌표 개수만큼 센서 그려주는거임
                    pygame.draw.circle(screen,(180,160,100),number,self.sensor_radius2,0)
            pygame.display.update()                     #화면 업데이트
            pygame.image.save(screen,"qqm_test version ["+(str)(self.countsensor)+"]"+(str)(self.countpicture) +".png")
                    #상태저장하는함수, 형식은 "이름" [센서갯수] "상태저장횟수".png로 저장이 된다.
            self.countpicture = self.countpicture + 1 
            run = False
        pygame.quit()
    
    def change_polygon(self,input_list):    
        self.polygon.clear()
        self.polygon = input_list


    def its_main(self):                 #이 함수 호출하면 이제 죄다 실행되는거임
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size, DOUBLEBUF)
        screen.fill((255,255,255))      #배경 흰색으로 채운거임
        #############################################이 위에는 이제 while문 위에 적히는 내용들 들어감
        self.runGame(screen)            #본격적인 파이게임작동..(while문에 들어가야할 내용들)

yeahgood = start(polygon_list,sensor_list,sensor_list2,radius,80)  #객체 생성


yeahgood.its_main()         #이거 호출하면이제 그냥 리스트대로 화면 캡처하고 저장해줌




