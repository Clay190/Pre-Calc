#Clay Kynor & Greg Phillips
#4.23.18
#jarProblem.py

from random import randint

N = 10
W = 8
RUNS = 1000

total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0

for i in range(0,RUNS):
    red = randint(0,N)
    green = N-red
    Pr = red/N
    Pg = green/N
    total1 += Pr
    total2 += Pg
    total3 += ((Pg)**2+(Pr)**2)
    total4 += (Pr**3) + (Pg**3)+(Pg*Pr*Pr*Pr)+(Pg*Pr*Pg*Pg)+(Pr*Pg*Pr*Pr)+(Pr*Pg*Pg*Pg)
    p1 = (red/N)*((red-1)/(N-1))*((red-2)/(N-2))
    p2 = (green/N)*((green-1)/(N-1))*((green-2)/(N-2))
    p3 = (green/N)*((red)/(N-1))*((green-1)/(N-2))*((green-2)/(N-3))
    p4 = (green/N)*((red)/(N-1))*((red-1)/(N-2))*((red-2)/(N-3))
    p5 = (red/N)*((green)/(N-1))*((green-1)/(N-2))*((green-2)/(N-3))
    p6 = (red/N)*((green)/(N-1))*((red-1)/(N-2))*((red-2)/(N-3))
    total5 += p1+p2+p3+p4+p5+p6

D1 = (total1/RUNS)*W
D2 = (total2/RUNS)*W
P = (total3/RUNS)*W-D1
R = ((total4/RUNS)*W)-D1
S = ((total5/RUNS)*W)-D1

print("Senerio 1:", total1/RUNS)
print("D for senerio 1 is", D1)
print("Senerio 2:", total2/RUNS)
print("D for senerio 2 is", D2)
print("Senerio 3:", total3/RUNS)
print("P for senerio 3 is", S)
print("Senerio 4:", total4/RUNS)
print("R for senerio 4 is", R)
print("Senerio 5:", total5/RUNS)
print("S for senerio 5 is", S)