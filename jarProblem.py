#Clay Kynor & Greg Phillips
#4.23.18
#jarProblem.py

from random import randint

N = randint(8,20)
W = randint(3,15)
D = 2*W

for i in range(0,N):
    red = randint(0,N)
    green = N-red
    
    Pr = (red/N)
    Pg = (green/N)
    
    print((Pr*W)-(Pg*(D-W)))
    


'''
N = int(input("Please enter a total amount of marbles (N value) between 8 and 20: "))
W = int(input("Please enter the money made when correct guess (W value) between 3 and 15: "))
D = W*2
print(D)
'''