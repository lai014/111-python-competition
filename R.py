def dfs(v):
    visited[v]=1
    for i in path[v]:
        if visited[i]==0:
            dfs(i)
n,m=map(int,input().split())
path=[[] for i in range(n+1)]
visited=[0 for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    path[x].append(y)
a,b=map(int,input().split())
dfs(a)
if visited[b]==1:
    print("Yes")
else:
    print("No")