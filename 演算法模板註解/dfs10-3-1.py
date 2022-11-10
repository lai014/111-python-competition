g={}
city={}
v=[0]*210
md=0
def getcityindex(p):
    if p not in city.keys():
        city[p]=len(city)
    return city[p]
def dfs(x,leval):
    global md
    for i in range(len(g[x])):
        if leval>md:
            md=leval
        target=g[x][i]
        if v[target]==1:
            continue

        v[target]=1
        dfs(target,leval+1)
m=int(input())
for i in range(m):
    a,b=input().split()
    a=getcityindex(a)
    b=getcityindex(b)
    if a in g.keys():
        g[a].append(b)
    else:
        g[a]=[b]
    if b in g.keys():
        g[b].append(a)
    else:
        g[b]=[a]
start=city[input()]
dfs(start,0)
print(md)
