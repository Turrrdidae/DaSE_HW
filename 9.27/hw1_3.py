s = input()
n = len(s)
i = 0
max = 0
flag = 0


while i < (n-1) :
    j = 1
    count = 1

    while (i+j) <= (n-1) and s[i] == s[i+j] :
        flag = 1
        count += 1
        j +=1
    
    if count > max :
        max = count
    
    i += 1


if flag :
    print("YES",end=" ")
    print(max)
else :
    print("NO")