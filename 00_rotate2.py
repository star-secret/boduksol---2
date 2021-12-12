import math

class rotate_polygon:
    def __init__(self, cp, base, height):   #자료형 = cp는 리스트, base는 숫자, height도 숫자
        self.centerpts = [cp[0],cp[1]]     #도형의 중심좌표 
        self.base = base        #도형의 밑변의 길이
        self.height = height    #도형의 높이
        self.pts = []           #도형의 각 좌표, 즉 [x,y]쌍을 저장할 리스트
        self.degree = 0
        self.rad = self.degree * (math.pi / 180.0)

    def print_triangle(self):
        print(self.centerpts[1])

    def its_triangle(self):
        x1= self.centerpts[0]
        y1= self.centerpts[1] + self.height*2/3
        x2 = self.centerpts[0] - self.base/2
        y2 = self.centerpts[1] -self.height/3
        x3= self.centerpts[0] + self.base/2
        y3 = self.centerpts[1] + self.height/3
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


    
sampletr = rotate_polygon([130,100],100,50)
sampletr.its_triangle()
sampletr.print_triangle()