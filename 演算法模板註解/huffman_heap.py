from heapq import * #載入heapq模組
hf=[0]*101     #hf節點
code=[0]*10    #hf編碼
def dfs(id,leval):   # hf[0]=權重 hf[1]=數值 hf[2]=字母 hf[3]=bool b[4]=le b[5]=ri
    if hf[id][3]==False: #如果不是業節點
        code[leval]="0"  #左邊碼為0
        dfs(hf[id][4],leval+1) #le遞迴
        code[leval]="1"  #右邊碼為1
        dfs(hf[id][5],leval+1) #ri遞迴
    else:  #如果是葉節點
        print(hf[id][2],end=" ")  #印出ch
        for i in range(leval): #印出目前的leval
            print(code[i],end=" ") 
        print()
c=["a","b","c","d","e"] #字母
w=[10,4,5,7,8] #權重
pq=[] #pq為占存
for i in range(len(c)): 
    node=(w[i],i,c[i],True,0,0) #宣告node
    hf[i]=node #將hf加入node
    heappush(pq,hf[i]) #導入pq
num=len(c) #num為數值
while len(pq)>1: #如果pq大於1
    a=heappop(pq) #第一小
    b=heappop(pq) #第二小
    node=(a[0]+b[0],num,None,False,a[1],b[1]) #新node
    hf[num]=node #加入hf
    heappush(pq,node) #導入pq
    num+=1 #數值+1
dfs(pq[0][1],0)

