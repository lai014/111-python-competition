import copy
list1=[int(i) for i in input().split()]
for _ in range(int(input())):
    list3=copy.copy(list1)
    list2=[int(i) for i in input().split()]
    a,b=0,0
    for i in range(4):
        if list3[i]==list2[i]:
            a+=1
            list3[i]=9999
            list2[i]=-9999
    for i in range(4):
        if list3[i] in list2:
            b+=1

            list2[list2.index(list3[i])]=-88888
            list3[i]=88888
    print("%dA%dB"%(a,b))