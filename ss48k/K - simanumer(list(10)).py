phone_number_list = []
appearance = []
searches = []
times = int(input())
for i in range(0,times):
    phone_numbers = str(input())
    phone_number_list.append(phone_numbers)
search_times = int(input())
for x in range(0,search_times):
    search = str(input())
    searches.append(search)

for s in searches:
    for item in phone_number_list:
        f = item.count(s)
        if f == 2:
            appearance.append(1)
        else:
            appearance.append(f)
i1 = 0
i2 = times
for l in appearance:
    if i2 != (times*search_times)+times:
        print (sum(appearance[i1:i2]), end="")
        print ("")
        i1 = i1 + times
        i2 = i2 + times
