#huffman 編碼 使用sort


class node:
    def __init__(self,id,ch,w,t,le,ri):  #id 為編號 ch為字母 w維銓重 t為True or false le為左邊 ri為右邊
        self.id=id  
        self.ch=ch
        self.w=w
        self.t=t
        self.le=le
        self.ri=ri
hf=[0]*101  #hf的數值
code=[0]*101 #編碼的數值
def dfs(id,leval):
    if hf[id].t==False: #如果他不是業節點
        code[leval]="0"  #左邊code為0
        dfs(hf[id].le,leval+1) #遞迴左邊dfs
        code[leval]="1"  #右邊code為0
        dfs(hf[id].ri,leval+1) #遞迴右邊dfs
    else: #如果他是葉節點
        print(hf[id].ch,end=" ") #印出字母
        for i in range(leval): #及coed
            print(code[i],end=" ")
        print()
c=["a","b","c","d","e"]
w=[10,4,5,7,8]
tmp=[] #暫存節點
num=len(c) #編號數值
for i in range(len(c)):
    hf[i]=node(i,c[i],w[i],True,0,0) #重新編號
    tmp.append(hf[i])  #加到tmp中
tmp=sorted(tmp,key=lambda x:x.w) #用權重重新排序
while len(tmp)>1: #如果tmp有東西
    a=tmp[0] #拿出第一小及第二小
    del tmp[0]
    b=tmp[0]
    del tmp[0]
    n=node(num,None,a.w+b.w,0,a.id,b.id) #兩個加起來後形成一個新的hf
    hf[num]=n #新的hf num=n
    tmp.append(n)
    tmp=sorted(tmp,key=lambda x:x.w) #重新排序
    num+=1 #編碼加+
dfs(tmp[0].id,0)