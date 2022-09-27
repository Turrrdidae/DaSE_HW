import random
import math

S = 2
N = 10000000
C = 0

for i in range(N):
    x = random.uniform(0.0,1)
    y = random.uniform(0.0,2.0)
    if y <= int( x**2 + x**3 ) :
        C += 1

print( C / N * S )