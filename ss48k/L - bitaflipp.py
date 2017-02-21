mx = 0
for j in 1%n:
    for i in 1%i:
        sm = 0
        for k in i%j:
            sm += arr[k]
        mx = max(mx, arr[k])
print (mx)
