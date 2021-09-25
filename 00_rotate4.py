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



    def its_triangle(self):     #삼각형 좌표 셋팅하는 함수임. 코드 작성할때 호출할 일 없을 것임.
                                # 따로 호출해도 될 것이지만 그러면 삼각형일때 이 함수, 사각형일 땐 또 따로 함수를 코드에 적어줘서 좌표를 셋팅해야함
                                #그래서 밑에 setting_pts함수를 이용하여서 도형 좌표 설정하면 되는 부분임.
        x1= self.centerpts[0]
        y1= self.centerpts[1] + self.height*2/3
        x2 = self.centerpts[0] - self.base/2
        y2 = self.centerpts[1] -self.height/3
        x3= self.centerpts[0] + self.base/2
        y3 = self.centerpts[1] - self.height/3
        nx1 = round(math.cos(self.rad)*(x1-self.centerpts[0]) - math.sin(self.rad)*(y1-self.centerpts[1])) + self.centerpts[0]
        ny1 = round(math.sin(self.rad)*(x1-self.centerpts[0]) + math.cos(self.rad)*(y1-self.centerpts[1])) + self.centerpts[1]
        nx2 = round(math.cos(self.rad)*(x2-self.centerpts[0]) - math.sin(self.rad)*(y2-self.centerpts[1])) + self.centerpts[0]
        ny2 = round(math.sin(self.rad)*(x2-self.centerpts[0]) + math.cos(self.rad)*(y2-self.centerpts[1])) + self.centerpts[1]
        nx3 = round(math.cos(self.rad)*(x3-self.centerpts[0]) - math.sin(self.rad)*(y3-self.centerpts[1])) + self.centerpts[0]
        ny3 = round(math.sin(self.rad)*(x3-self.centerpts[0]) + math.cos(self.rad)*(y3-self.centerpts[1])) + self.centerpts[1]
        self.pts.append([nx1,ny1])
        self.pts.append([nx2,ny2])
        self.pts.append([nx3,ny3])
        print(self.pts)

    def its_rectangle(self):    #사각형 좌표 셋팅하는 함수
        x1= self.centerpts[0] - self.base/2
        y1= self.centerpts[1] - self.height/2
        x2 = self.centerpts[0] + self.base/2
        y2 = self.centerpts[1] - self.height/2
        x3= self.centerpts[0] + self.base/2
        y3 = self.centerpts[1] + self.height/2
        x4= self.centerpts[0] - self.base/2
        y4 = self.centerpts[1] + self.height/2
        nx1 = round(math.cos(self.rad)*(x1-self.centerpts[0]) - math.sin(self.rad)*(y1-self.centerpts[1])) + self.centerpts[0]
        ny1 = round(math.sin(self.rad)*(x1-self.centerpts[0]) + math.cos(self.rad)*(y1-self.centerpts[1])) + self.centerpts[1]
        nx2 = round(math.cos(self.rad)*(x2-self.centerpts[0]) - math.sin(self.rad)*(y2-self.centerpts[1])) + self.centerpts[0]
        ny2 = round(math.sin(self.rad)*(x2-self.centerpts[0]) + math.cos(self.rad)*(y2-self.centerpts[1])) + self.centerpts[1]
        nx3 = round(math.cos(self.rad)*(x3-self.centerpts[0]) - math.sin(self.rad)*(y3-self.centerpts[1])) + self.centerpts[0]
        ny3 = round(math.sin(self.rad)*(x3-self.centerpts[0]) + math.cos(self.rad)*(y3-self.centerpts[1])) + self.centerpts[1]
        nx4 = round(math.cos(self.rad)*(x4-self.centerpts[0]) - math.sin(self.rad)*(y4-self.centerpts[1])) + self.centerpts[0]
        ny4 = round(math.sin(self.rad)*(x4-self.centerpts[0]) + math.cos(self.rad)*(y4-self.centerpts[1])) + self.centerpts[1]
        self.pts.append([nx1,ny1])
        self.pts.append([nx2,ny2])
        self.pts.append([nx3,ny3])
        self.pts.append([nx4,ny4])
        print(self.pts)

    def return_pts(self):   #도형의 좌표를 리스트로 반환하는 함수
        return self.pts

    def change_degree(self, ch_degree):     #도형의 각도를 변환하는 함수. 기본셋팅은 0도. change_degree(원하는각도)로 호출해서 각도 변환 가능
        self.degree= ch_degree
        self.rad = self.degree * (math.pi / 180.0)
        self.pts.clear()
        if self.number == 1:
            self.its_triangle()
        elif self.number ==2:
            self.its_rectangle()
        else:
            print("오류")

    def setting_pts(self):      #도형의 각 좌표들을 셋팅하는 함수.
        if self.number == 1:    #삼각형
            self.its_triangle()
        elif self.number ==2:   #사각형
            self.its_rectangle()
        else:
            print("오류")

    def draw_pts(self,screen):  #도형 그리는 함수. pygame의 screen객체를 받아와야함.
        if self.number == 1 or self.number ==2:
            pygame.draw.polygon(screen,(110,110,100),self.return_pts())     #(110,110,100)은 도형의 색을 의미함
        elif self.number == 3:
            pygame.draw.circle(screen,(255,200,50),self.centerpts,self.radius)
        #pygame.draw.polygon(screen,(110,110,100),self.return_pts(),3) 이런식으로 작성시 도형의 내부색칠 안하고 테두리만 색 입힐 수 있다

pygame.init()      #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 1000   #가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game")

# 배경 이미지 불러오기
background = pygame.image.load("background.png")

#각 도형마다 rotate_polygon 객체를 생성해야함.
sampletr = rotate_polygon([230,100],200,50,2)   #사각형 생성    [중심좌표],밑변,높이,2를 입력해줘야함 (2가 사각형임을 의미)
sampletr.change_degree(20)  #사각형 회전
sampletr.draw_pts(screen)   #그리기

sampletr2 = rotate_polygon([430,100],100,60,1)  #삼각형 생성   [중심좌표],밑변,높이,1를 입력해줘야함 (1은 삼각형임을 의미)
sampletr2.change_degree(77)     #삼각형 회전
sampletr2.draw_pts(screen)

sampletr3 = rotate_polygon([150,300],10,0,3)    #원 생성        [중심좌표],반지름,0,3을 의미해야함. (3은 삼각형을 의미)
sampletr3.draw_pts(screen)

running = True  #게임이 진행중인지 확인
while running:
    for event in pygame.event.get():    #이벤트(마우스,키보드) 체크
        if event.type == pygame.QUIT:    #일반적인 창에 있는 x버튼을 눌렀을 때 발생하는 이벤트
            running = False     #게임 진행 중 아님


    pygame.display.update() #게임화면 다시 그리기 (파이게임에서는 매 프레임마다 화면을 다시 그려줘야함)
# pygame 종료
pygame.quit()
sys.exit()

