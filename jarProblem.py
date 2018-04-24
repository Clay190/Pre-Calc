#Clay Kynor & Greg Phillips
#4.23.18
#jarProblem.py

from random import randint

N = randint(8,20)
W = randint(3,15)
D = .5*W

red = randint(0,N)
green = N-red
num = randint(0,N)

if num >= red:
    print("Red ball is picked: ")
    print(red)
    print(num)
    
    
#list of 10 values (r or g) then gen a random number/value if that is an r or g you win or lose

'''
N = int(input("Please enter a total amount of marbles (N value) between 8 and 20: "))
W = int(input("Please enter the money made when correct guess (W value) between 3 and 15: "))
D = W*2
print(D)
'''