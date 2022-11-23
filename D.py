a=int(input())
list1=[int(i) for i in input().split()]
list1.sort()
if sum(list1)%2==0:
    print(sum(list1))
else:
    for i in list1:
        if i%2!=0:
            t=sum(list1)-i
            break
    print(t)