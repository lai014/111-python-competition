a,b,c,d=map(int,input().split())
list1=[]
for i in range(a):
    s=[int(i) for i in input().split()]
    list1.append(s)
list2=[]
for j in range(c):
    s=[int(i) for i in input().split()]
    list2.append(s)
list3=[]
f=0
for i in range((b)):
    for g in range((d)):
        list3.append([])    
        for k in range(a):
            for j in range((c)):
                list3[f].append(list1[k][i]*list2[j][g])
        f+=1
list4=[]
for i in range(len(list3[0])):
    list4.append([])
    for j in range(len(list3)):
        list4[i].append(list3[j][i])
for i in list4:
    print(*i)