a=input()
list1=[int(i) for i in input().split()]
s=0
for i in range(len(list1)):
    for j in list1[:i]:
        if j>list1[i]:
            s+=1
print(s)