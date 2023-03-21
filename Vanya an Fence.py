import math

x = str(input()).split()
n = int(x[0])
h = int(x[1])
y = str(input()).split()
count = 0

for i in range (0,len(y)):
    if int(y[i])<=h:
        count += 1
    elif int(y[i])>h:
        z = int(y[i])/h
        count = count + math.ceil(z)
        
print(count)
                