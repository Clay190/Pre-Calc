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

'''

#5a)

from random import randint

N = 10
W = 8
RUNS = 10

total = 0

for i in range(0,RUNS):
    green = randint(0,N)
    red = N-green
    p1 = (red/N)*((red-1)/(N-1))*((red-2)/(N-2))
    p2 = (green/N)*((green-1)/(N-1))*((green-2)/(N-2))
    p3 = (green/N)*((red)/(N-1))*((green-1)/(N-2))*((green-2)/(N-3))
    p4 = (green/N)*((red)/(N-1))*((red-1)/(N-2))*((red-2)/(N-3))
    p5 = (red/N)*((green)/(N-1))*((green-1)/(N-2))*((green-2)/(N-3))
    p6 = (red/N)*((green)/(N-1))*((red-1)/(N-2))*((red-2)/(N-3))
    total += p1+p2+p3+p4+p5+p6
    
print(total/RUNS)

