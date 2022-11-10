class point:
    def __init__(self,r,c,dis):
        self.r=r
        self.c=c
        self.dis=dis
def bound(row,col,nr,nc):
    if row>0 and row<=nr and col>0 and col<=nc:
        return 1
    else:
        return 0
map1=[[0]*101 for i in range(101)]
val=[[0]*101 for i in range(101)]
gor=[0,1,0,-1]
goc=[1,0,-1,0]
myq=[]
r,c=map(int,input().split())
for i in range(1,r+1):
    line=input().split()
    for j in range(c):
        map1[i][j+1]=int(line[j])
sr,sc=map(int,input().split())
myp=point(sr,sc,1)
val[myp.r][myp.c]=1
myq.append(myp)
while len(myq)>0:
    nextp=myq[0]
    del myq[0]
    for i in range(4):
        if bound(nextp.r+gor[i],nextp.c+goc[i],r,c) and map1[nextp.r+gor[i]][nextp.c+goc[i]]==1 and val[nextp.r+gor[i]][nextp.c+goc[i]]==0:
            val[nextp.r+gor[i]][nextp.c+goc[i]]=nextp.dis+1
            tmp=point(0,0,0)
            tmp.r=nextp.r+gor[i]
            tmp.c=nextp.c+goc[i]
            tmp.dis=nextp.dis+1
            myq.append(tmp)
for i in range(r):
    for j in range(c):
        print(val[i+1][j+1],end=" ")
    print()