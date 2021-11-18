from itertools import combinations_with_replacement



class init_sensor:
    def __init__(self, cost, price_list, area_list, number_of_sensor):
        # 비용상한선,  센서의 가격 리스트, 센서마다 탐지하는 영역의 넓이 리스트, 배치에 사용할 총 센서의 개수를 입력받아야 함
        self.cost = cost
        
        self.price_list = price_list
        self.area_list = area_list
        self.number_of_sensor = number_of_sensor
        self.sensor_make = set(combinations_with_replacement(sensor_price, num))
        self.sensor = list(self.sensor_make)
        self.area = []
        self.price =[]
        self.index = 0 #최종 선택된 센서 조합의 인덱스를 저장할 변수
        
        self.set_init()
        self.limit_cost()
        self. select_sensor()
        self.print_sensor()
        
    def set_init(self):     #센서 조합에 대응 되는 넓이와 가격 리스트 셋팅
        for m in self.sensor:
            pricesum = 0
            areasum = 0
            for k in m:
                pricesum += k   #센서조합의 인덱스에 대응되는 가격의 합
                make_index=0
                for n in sensor_price:
                    if(k == n):
                        areasum += sensor_area[make_index]      #센서조합의 인덱스에 대응되는 넓이의 합
                    make_index += 1
            self.price.append(pricesum)
            self.area.append(areasum)
    
    def limit_cost(self): #비용한도를 초과하는 센서 삭제
        check = []
        for m in range (len(self.sensor)):
            if(self.price[m] > self.cost):
                check.append(m)
        reverse_check = list(reversed(check))      
        for m in range (len(check)):
            del self.sensor[reverse_check[m]]
            del self.area[reverse_check[m]]
            del self.price[reverse_check[m]]
    
    def select_sensor(self): #비용한도를 넘지 않으면서 관심영역의 넓이를 넘지 않는 최대 넓이의 센서조합 선택
        max = self.area[0]
        for m in range (len(self.sensor)):
            if((max < self.area[m])):
                max = self.area[m]
                self.index = m
    
    def print_sensor(self): #선택된 센서관련 정보 출력
        print(self.area[self.index])
        print(self.sensor[self.index])
        print(self.price[self.index])
        
        
#작성한 클래스 테스트
        
cost = 17500 #비용한도

sensor_price = [ 1100, 2700, 3300, 4000, 5678 ]     # 센서의 가격
sensor_area = [ 600, 2000, 2400, 2900, 3987]    #센서의 가격에 대응하는 넓이
init_area = 12345
num = 7

yeahgood = init_sensor(cost,sensor_price,sensor_area,num)

