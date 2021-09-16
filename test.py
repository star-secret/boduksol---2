r = float(input())
R = float(input())
n = abs(0.83*((R**2)/(r**2)) - 1.9)
p = int(n)*100*(r**2)/(R**2)

print(str(int(n))+" smaller circles cover " + str(format(p,".2f")) + "% of the larger circle")
