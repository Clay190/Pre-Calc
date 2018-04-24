#Clay Kynor & Greg Phillips
#4.23.18
#jarProblem.py

from random import randint

N = 10
W = 8
RUNS = 1000

total = 0

for i in range(0,RUNS):
    green = randint(0,N)
    red = 1-green
    total += ((green/N)**2+(red/N)**2)

print(total/RUNS)
