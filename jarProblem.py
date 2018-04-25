#Clay Kynor & Greg Phillips
#4.23.18
#jarProblem.py

'''
#1a)

from random import randint

N = 10
W = 8
RUNS = 1000

total = 0

for i in range(0,RUNS):
    red = randint(0,N)
    green = N-red
    total += (red/N)

D = (total/RUNS)*W
print(total/RUNS)

#2a)
from random import randint

N = 10
W = 8
RUNS = 1000

total = 0

for i in range(0,RUNS):
    green = randint(0,N)
    red = N-green
    total += (green/N)

D = (total/RUNS)*W
print(total/RUNS)

#3a)
from random import randint

N = 10
W = 8
RUNS = 1000

total = 0

for i in range(0,RUNS):
    green = randint(0,N)
    red = N-green
    total += ((green/N)**2+(red/N)**2)

print(total/RUNS)

'''

#4a)
from random import randint

N = 10
W = 8
RUNS = 1000

total = 0

for i in range(0,RUNS):
    green = randint(0,N)
    red = N-green
    Pr = red/N
    Pg = green/N
    p1 = Pr*Pr*Pr
    p2 = Pg*Pg*Pg
    p3 = Pg*Pr*Pr*Pr
    p4 = Pg*Pr*Pg*Pg
    p5 = Pr*Pg*Pr*Pr
    p6 = Pr*Pg*Pg*Pg
    total += p1+p2+p3+p4+p5+p6
    
print(total/RUNS)



