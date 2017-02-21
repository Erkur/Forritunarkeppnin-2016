n = int(input())
ages = []
ages_archive = []
for i in range(0, n):
    a = str(input(""))
    if a[0] == "A":
        ages.append(int(a[2:]))
    elif a[0] == "R":
        ages.remove(int(a[2:]))     
    if not ages:
        ages_archive.append("0")
    else:
        ages_archive.append((min(ages), max(ages), "%.6f" % (sum(ages) / float(len(ages)))))
for j in ages_archive:
    if j == "0":
        print ("-1 -1 -1")
    else:
        print (' '.join(map(str, j)))
