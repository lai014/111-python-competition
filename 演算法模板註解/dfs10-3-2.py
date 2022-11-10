import sys

g={}
city={}
v=[0]*27
isloop=False
def getcityindex(p):
    if p not in city.keys():
        city[p]=len(city)
    return city[p]
def dfs(x,start):
    global isloop
    if x in g.keys():
        for target in g[x]:
            if target==start:
                isloop=True
                return 
            if v[target]==1:continue
            v[target]=1
            dfs(target,start)
            v[target]=0
for line in sys.stdin:
    g.clear()
    v=[0]*27
    n=int(line)
    for i in range(n):
        a,b=input().split()
        a=getcityindex(a)
        b=getcityindex(b)
        if a in g.keys():
            g[a].append(b)
        else:
            g[a]=[b]
    for item in g.keys():
        dfs(item,item)
        if isloop:break
    if isloop:print("yes")
    else:print("no")
