import pygame,sys
import math

#5~80까지가 도형변환에 관련된 함수임. 이거 어떻게 사용해야하는지는 107번쨰 줄부터 참고바람.
#5~94는 굳이 안봐도 되고 그냥 이거 통째로 복붙해놓고 107~119만 보고 어떻게 쓰는지 알면 되긴 함. 색 바꾸고 싶으면 88번째 줄인 draw_pts함수에서 바꾸면 된다.
class rotate_polygon:
    def __init__(self, cp, base, height,number):   #자료형 = cp는 리스트, base는 숫자, height도 숫자, number은 숫자
        self.centerpts = [cp[0],cp[1]]     #도형의 중심좌표 
        self.base = base        #도형의 밑변의 길이
        self.height = height    #도형의 높이
        self.pts = []           #도형의 각 좌표, 즉 [x,y]쌍을 저장할 리스트, 도형의 중심, 밑변, 높이만 정해주면 좌표는 함수로 알아서 설정
        self.degree = 0         #도형의 회전 각을 의미. 초기에는 0도로 설정.
        self.rad = self.degree * (math.pi / 180.0)  #rad 수식
        self.number = number        # 도형의 중심, 밑변, 높이를 가지고 어떤 도형을 그릴지 선택해야함
                                    # number가 1이면 삼각형, 2면 사각형,3이면 원을 의미
        if self.number == 3 and self.height ==0:    #원을 입력하고 싶은 경우, cp, base,0,3을 생성자로 입력해주어야함. base가 radius가 된다.
            self.radius = base          #number가 3인경우에만 쓰임
        if self.number == 1 or self.number ==2:
            self.setting_pts()
