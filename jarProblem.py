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
    total4 += (Pr*Pr*Pr) + (Pg*Pg*Pg)+(Pg*Pr*Pr*Pr)+(Pg*Pr*Pg*Pg)+(Pr*Pg*Pr*Pr)+(Pr*Pg*Pg*Pg)
    p1 = (red/N)*((red-1)/(N-1))*((red-2)/(N-2))
    p2 = (green/N)*((green-1)/(N-1))*((green-2)/(N-2))
    p3 = (green/N)*((red)/(N-1))*((green-1)/(N-2))*((green-2)/(N-3))
    p4 = (green/N)*((red)/(N-1))*((red-1)/(N-2))*((red-2)/(N-3))
    p5 = (red/N)*((green)/(N-1))*((green-1)/(N-2))*((green-2)/(N-3))
    p6 = (red/N)*((green)/(N-1))*((red-1)/(N-2))*((red-2)/(N-3))
    total5 += p1+p2+p3+p4+p5+p6

D = (total1/RUNS)*W
D2 = (total2/RUNS)*W
print("Senerio 1", total1/RUNS)

    
