import pygame,sys
import math


class rotate_polygon:
    def __init__(self, cp, base, height,number):   #자료형 = cp는 리스트, base는 숫자, height도 숫자, number은 숫자
        self.centerpts = [cp[0],cp[1]]     #도형의 중심좌표 
        self.base = base        #도형의 밑변의 길이
        self.height = height    #도형의 높이
        self.pts = []           #도형의 각 좌표, 즉 [x,y]쌍을 저장할 리스트, 도형의 중심, 밑변, 높이만 정해주면 좌표는 함수로 알아서 설정
        self.degree = 0         #도형의 회전 각을 의미. 초기에는 0도로 설정.
        self.rad = self.degree * (math.pi / 180.0)  #rad 수식
        self.number = number        # 도형의 중심, 밑변, 높이를 가지고 어떤 도형을 그릴지 선택해야함
                                    # number가 1이면 삼각형, 2면 사각형

    def print_triangle(self):       
        print(self.centerpts[1])

    def its_triangle(self):
        x1= self.centerpts[0]
        y1= self.centerpts[1] + self.height*2/3
        x2 = self.centerpts[0] - self.base/2
        y2 = self.centerpts[1] -self.height/3
        x3= self.centerpts[0] + self.base/2
        y3 = self.centerpts[1] - self.height/3
        nx1 = round(math.cos(self.rad)*(x1-self.centerpts[0]) - math.sin(self.rad)*(y1-self.centerpts[1])) + self.centerpts[0]
        ny1 = round(math.sin(self.rad)*(x1-self.centerpts[0]) - math.cos(self.rad)*(y1-self.centerpts[1])) + self.centerpts[1]
        nx2 = round(math.cos(self.rad)*(x2-self.centerpts[0]) - math.sin(self.rad)*(y2-self.centerpts[1])) + self.centerpts[0]
        ny2 = round(math.sin(self.rad)*(x2-self.centerpts[0]) - math.cos(self.rad)*(y2-self.centerpts[1])) + self.centerpts[1]
        nx3 = round(math.cos(self.rad)*(x3-self.centerpts[0]) - math.sin(self.rad)*(y3-self.centerpts[1])) + self.centerpts[0]
        ny3 = round(math.sin(self.rad)*(x3-self.centerpts[0]) - math.cos(self.rad)*(y3-self.centerpts[1])) + self.centerpts[1]
        self.pts.append([nx1,ny1])
        self.pts.append([nx2,ny2])
        self.pts.append([nx3,ny3])
        print(self.pts)

    def its_rectangle(self):
        x1= self.centerpts[0] - self.base/2
        y1= self.centerpts[1] - self.height/2
        x2 = self.centerpts[0] + self.base/2
        y2 = self.centerpts[1] - self.height/2
        x3= self.centerpts[0] + self.base/2
        y3 = self.centerpts[1] + self.height/2
        x4= self.centerpts[0] - self.base/2
        y4 = self.centerpts[1] + self.height/2
        nx1 = round(math.cos(self.rad)*(x1-self.centerpts[0]) - math.sin(self.rad)*(y1-self.centerpts[1])) + self.centerpts[0]
        ny1 = round(math.sin(self.rad)*(x1-self.centerpts[0]) - math.cos(self.rad)*(y1-self.centerpts[1])) + self.centerpts[1]
        nx2 = round(math.cos(self.rad)*(x2-self.centerpts[0]) - math.sin(self.rad)*(y2-self.centerpts[1])) + self.centerpts[0]
        ny2 = round(math.sin(self.rad)*(x2-self.centerpts[0]) - math.cos(self.rad)*(y2-self.centerpts[1])) + self.centerpts[1]
        nx3 = round(math.cos(self.rad)*(x3-self.centerpts[0]) - math.sin(self.rad)*(y3-self.centerpts[1])) + self.centerpts[0]
        ny3 = round(math.sin(self.rad)*(x3-self.centerpts[0]) - math.cos(self.rad)*(y3-self.centerpts[1])) + self.centerpts[1]
        nx4 = round(math.cos(self.rad)*(x4-self.centerpts[0]) - math.sin(self.rad)*(y4-self.centerpts[1])) + self.centerpts[0]
        ny4 = round(math.sin(self.rad)*(x4-self.centerpts[0]) - math.cos(self.rad)*(y4-self.centerpts[1])) + self.centerpts[1]
        self.pts.append([nx1,ny1])
        self.pts.append([nx2,ny2])
        self.pts.append([nx3,ny3])
        self.pts.append([nx4,ny4])
        print(self.pts)

    def return_pts(self):
        return self.pts

    def change_degree(self, ch_degree):
        self.degree= ch_degree
        self.rad = self.degree * (math.pi / 180.0)
        self.pts.clear()
        if self.number == 1:
            self.its_triangle()
        elif self.number ==2:
            self.its_rectangle()
        else:
            print("오류")

    def setting_pts(self):
        if self.number == 1:
            self.its_triangle()
        elif self.number ==2:
            self.its_rectangle()
        else:
            print("오류")
pygame.init()      #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 1000   #가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game")

# 배경 이미지 불러오기
background = pygame.image.load("background.png")

#이벤트 루프 - 사용자가 키를 입력하거나 마우스를 움직이거나 하는
#동작을 계속 감지하는 이벤트 루프가 있음
#파이 게임에서는 이 이벤트루프가 계속 실행되고 있어야 창이 꺼지지 않음


sampletr = rotate_polygon([230,100],200,50,1)
sampletr.setting_pts()
sampletr.change_degree(30)
pygame.draw.polygon(screen,(110,110,100),sampletr.return_pts())

running = True  #게임이 진행중인지 확인
while running:
    for event in pygame.event.get():    #이벤트(마우스,키보드) 체크
        if event.type == pygame.QUIT:    #일반적인 창에 있는 x버튼을 눌렀을 때 발생하는 이벤트
            running = False     #게임 진행 중 아님


    pygame.display.update() #게임화면 다시 그리기 (파이게임에서는 매 프레임마다 화면을 다시 그려줘야함)
# pygame 종료
pygame.quit()
sys.exit()

