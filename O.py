a=list(input())
b=list(input())
c=list(input())
list1=[]
for i in range(len(a)+1):
    list1.append([])
    for j in range(len(b)+1):
        list1[i].append([])
        for k in range(len(c)+1):
            list1[i][j].append(0)
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        for k in range(1,len(c)+1):
            if a[i-1]==b[j-1] and b[j-1]==c[k-1]:
                list1[i][j][k]=list1[i-1][j-1][k-1]+1
            else:
                list1[i][j][k]=max(list1[i-1][j][k],list1[i][j-1][k],list1[i][j][k-1])
print(list1[-1][-1][-1])