n = int(input())
x=[]
for i in range(0,n):
    name=str(input())
    city=str(input())
    x.append(city)

dict = {}
for city in x:
    keys = dict.keys()
    if city in keys:
        dict[city] += 1
    else:
        dict[city] = 1
    
for key,val in dict.items():
    print (key, val)
