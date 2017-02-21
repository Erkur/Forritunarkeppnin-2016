phone_number_list = ""
appearance = ""
searches = ""
times = int(input())
for i in range(0,times):
    phone_numbers = str(input())
    phone_number_list += phone_numbers + ","
search_times = int(input())
for x in range(0,search_times):
    search = str(input())
    searches += search + ","

for s in searches.split(','):
   for item in phone_number_list.split(','):
        f = item.count(s)
        if f == 2:
            f = f-1
            appearance = appearance + str(f) + ","
        else:
            appearance = appearance + str(f) + ","
i1 = 0
i2 = times
new = appearance.split(',')
del new[-1]
new = list(map(int, new))
for l in new:
    if i2 != (times*search_times)+times:
        print (sum(new[i1:i2]), end="")
        print ("")
        i1 = i1 + times
        i2 = i2 + times
