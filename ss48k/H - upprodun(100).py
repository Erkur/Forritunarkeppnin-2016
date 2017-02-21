x = int(input())
y = int(input())
l = []
newl = []
d = y/x
for i in range(0,x):
    l.append(y/x)
for m in l:
    new = round(m)
    if (sum(newl) < y):
        newl.append(new)
if (sum(newl) != y):
    for j in range(0,len(newl)):
        if (sum(newl) < y):
            newl[j] = newl[j] + 1
        elif(sum(newl) > y):
            newl[j] = newl[j] - 1
for i in newl:
    print ("*"*i)
