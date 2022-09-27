#循环迭代
c = 2
g = 1

while(abs(g * g - c) > 0.0001):
    g += 0.00001

print("%.5f" %g)


#二分法
c = 2
left = 0
right = c
g = (left + right)/2

while(abs(g * g - c) > 0.0000000001):
    if(g * g < c):
        left = g
    else :
        right = g
    g = (left + right)/2

print("%.13f" %g)


#牛顿法
c = 2
g = c/2

while(abs(g * g - c) > 0.00000000001):
    g = (g + c/g)/2

print("%.13f" %g)