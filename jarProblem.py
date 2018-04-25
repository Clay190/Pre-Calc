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
RUNS = 1

total = 10

for i in range(0,RUNS):
    green = randint(0,N)
    red = N-green
    Pr = red/N
    Pg = green/N
    p1 = Pr**2
    p2 = Pg**2
    
    
    print(p1+p2+p3+p4+p5+p6)

print(total/RUNS)



