class checking:
    def __init__(self, radius1,cost1, radius2,cost2):   #센서의 반지름과 각 반지름의 cost를 입력받음
        if cost1 > cost2:
            self.c1 = cost1
            self.c2 = cost2
            self.r1= radius1
            self.r2 = radius2
        else:
            self.c1 = cost2
            self.r1= radius2
            self.c1 = cost1
            self.r2 = radius1
        self.a1 = radius1*radius1*3.14
        self.a2 = radius2*radius2*3.14
        self.now_area

    def check(self,area):     # 현재 화면에서 센서가 커버하고있는 총 면적을 입력받음
                                     # 면적이 큰 센서부터 배치를 시작할 것인데, 큰 센서를 배치하고 있는 도중에
                                     #  면적당 비용 효율이 좋지 않으면, 1을 반환, 그러면 이제부터 작은 센서를 배치하여야 함
                                     # 면적당 비용 효율이 여전히 좋으면 0을 반화느 그러면 계속 큰 센서를 배치하면 됨
        diff_area = area - self.now_area
        self.now_area = area
        if (diff_area/self.c1 < self.a2/self.c2):
            return 1
        else:
            return 0