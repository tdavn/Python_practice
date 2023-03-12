number = [65, 700, 1500, 1, 0, 44.5, -0.1]
minx = number[0]

for i in range(0,len(number)):
    if minx > number[i]:
        minx = number[i]

print(minx)
