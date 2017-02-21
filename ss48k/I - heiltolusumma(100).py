nr = int(input(""))
if nr >= 1:
    print (nr * (nr + 1) // 2)
else:
    nr = -nr
    print (-nr * (nr + 1) // 2 + 1)

