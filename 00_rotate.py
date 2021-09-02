import pygame,sys
import math
pygame.init()      #초기화 (반드시 필요)
'''
class func_rotate:
    def __init__(self, centerpts, polygonpts): 
        self.centerpt= centerpts
        self.polygonpt = polygonpts

    def runGame(self, centerpts,polygonpts, degree):  #파이게임의 실행과 이미지 저장
        self.centerpt = centerpts
        self.polygonpt = polygonpts
        rad = degree * (math.pi / 180.0)
        nx = round(math.cos(rad)*x - math.sin(rad)*y)
        ny = round(math.sin(rad)*x + math.cos(rad)*y)
        return (nx,ny)
        
gogo = func_rotate((100,100),(200,200))'''
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

polygonpts1=[100,50]
polygonpts2=[50,125]
polygonpts3=[150,125]
centerppp=[100,100]
ppp=[polygonpts1,polygonpts2]
print(ppp[0][1])
degree = 90
rad = degree * (math.pi / 180.0)
nx1 = round(math.cos(rad)*(polygonpts1[0]-centerppp[0]) - math.sin(rad)*(polygonpts1[1]-centerppp[1])) + centerppp[0]
ny1 = round(math.sin(rad)*(polygonpts1[0]-centerppp[0]) + math.cos(rad)*(polygonpts1[1]-centerppp[1])) + centerppp[1]
nx2 = round(math.cos(rad)*(polygonpts2[0]-centerppp[0]) - math.sin(rad)*(polygonpts2[1]-centerppp[1])) + centerppp[0]
ny2 = round(math.sin(rad)*(polygonpts2[0]-centerppp[0]) + math.cos(rad)*(polygonpts2[1]-centerppp[1])) + centerppp[1]
nx3 = round(math.cos(rad)*(polygonpts3[0]-centerppp[0]) - math.sin(rad)*(polygonpts3[1]-centerppp[1])) + centerppp[0]
ny3 = round(math.sin(rad)*(polygonpts3[0]-centerppp[0]) + math.cos(rad)*(polygonpts3[1]-centerppp[1])) + centerppp[1]
pygame.draw.polygon(screen,(110,110,100),[[nx1,ny1],[nx2,ny2],[nx3,ny3]])
running = True  #게임이 진행중인지 확인
while running:
    for event in pygame.event.get():    #이벤트(마우스,키보드) 체크
        if event.type == pygame.QUIT:    #일반적인 창에 있는 x버튼을 눌렀을 때 발생하는 이벤트
            running = False     #게임 진행 중 아님


    pygame.display.update() #게임화면 다시 그리기 (파이게임에서는 매 프레임마다 화면을 다시 그려줘야함)
# pygame 종료
pygame.quit()
sys.exit()

