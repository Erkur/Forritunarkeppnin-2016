x, y = map(int, input().split())
if (x % 2 == 0 and y % 2 == 0):
    print (x * y)
elif (x % 2 != 0 or y % 2 != 0):
    print (x*y-1)
else:
    print (x*y-2) 
