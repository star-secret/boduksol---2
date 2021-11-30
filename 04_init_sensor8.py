from itertools import combinations_with_replacement


        
def set_init(cost, price_list, area_list):     
    # 비용상한선,  센서의 가격 리스트, 센서마다 탐지하는 영역의 넓이 리스트 입력받기
    final_area = []
    final_sensor = []
    final_price = []
    cost = cost
    area_list = area_list
    
    num=1 #이것은 사용하는 센서의 종류, while문을 통해서 num이 계속 증가함.즉 배치에 사용하는 센서의 개수가 계속 늘어남.
    while True:
        
        index = 0
        price = []
        area = []
        sensor_make = set(combinations_with_replacement(price_list, num))
        sensor = list(sensor_make)
        for m in sensor:
            pricesum = 0
            areasum = 0
            for k in m:
                pricesum += k   #센서조합의 인덱스에 대응되는 가격의 합
                make_index=0
                for n in price_list:
                    if(k == n):
                        areasum += area_list[make_index]      #센서조합의 인덱스에 대응되는 넓이의 합
                    make_index += 1
            price.append(pricesum)
            area.append(areasum)
            
        #비용상한선을 넘는 센서를 확인하고 제거하는 과정
        check = []
        for m in range (len(sensor)):
            if(price[m] > cost):
                check.append(m)
        reverse_check = list(reversed(check))      
        for m in range (len(check)):
            del sensor[reverse_check[m]]
            del area[reverse_check[m]]
            del price[reverse_check[m]]
        
        #센서의 개수가 m개일 때 가능한 모든 센서 조합의 비용의 합이 비용상한선을 초과하면 더이상 센서의 개수를 증가시키지 않고 반복문을 종료    
        if(len(sensor) == 0):
            break
        
        #비용상한선을 넘지않는 센서 조합중 넓이 합이 최고인 센서 조합 탐지
        max = area[0]
        for m in range (len(sensor)):
            if((max < area[m])):
                max = area[m]
                index = m
        final_area.append(area[index])
        final_sensor.append(sensor[index])
        final_price.append(price[index])
        
        num += 1
        
    #while문이 끝나고 나면 센서의 개수가 3,4,5,6개 등등일 때, 각각의 개수에 따른 최적의 배치를또 비교 함. 그 중 넓이 합이 최고인 것을 선택    
    new_max = final_area[0]   
    new_sensor = []
    new_price = 0
    for i in range (len(final_area)):
        if(new_max<final_area[i]):
            new_max = final_area[i]
            new_sensor=final_sensor[i]
            new_price = final_price[i]
    print("총 넓이 : " + (str)(new_max))
    print(new_sensor)        
    print("총 비용 : "+(str)(new_price))

#작성한 함수 테스트
        
cost = 16900 #비용한도

sensor_price = [ 1100, 2700, 3300, 4000, 5678 ]     # 센서의 가격
sensor_area = [ 600, 2000, 2400, 2900, 3987]    #센서의 가격에 대응하는 넓이


set_init(cost,sensor_price,sensor_area)