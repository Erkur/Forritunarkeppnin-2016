#lýsandi breytu nöfn hvað?
problems_count=int(input())
teams_count=int(input())
problem_names=str(input()).split(" ")
l = []
c = []
maxed = []
for i in range(0,teams_count):
    team_points=str(input()).split(" ")
    l.append(team_points)
for x in l:
    m = list(map(int, x))
    c.append(m)
n = list(map(list, zip(*c)))
for s in n:
    maxed.append(sum(s))
m = max(maxed)
xd = [i for i, j in enumerate(maxed) if j == m]
for q in xd:
    print (problem_names[q])
