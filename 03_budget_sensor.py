class budget_check:
    def __init__(self, budget,radius1,cost1, radius2,cost2):
        self.budget =budget
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

        self.combination = []
        self.check()
    def check(self):
        num1 = 10
        num2 = 0
        num3 = 0
        while (num1 != 0):
            num1 = (self.budget // self.c1) - num3
            num2 = (self.budget - (num1*self.c1)) // self.c2
            self.combination.append([num1, num2])
            num3 += 1
    def print_comb(self):
        for i in range(len(self.combination)):
            print("조합 " + (str)(i+1))
            print("반지름이 "+(str)(self.r1) +"인 센서 개수 : " + (str)(self.combination[i][0])  )
            print("반지름이 "+(str)(self.r2) +"인 센서 개수 : " + (str)(self.combination[i][1]))

oh_nice =  budget_check(100,10,20,5,13)
oh_nice.print_comb()
