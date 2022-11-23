input()
list1=[int(i) for i in input().split()]
for i in list1:
    s=i
    for j in [2,3,5]:
        while s%j==0:
            s=s//j
    if s==1:
        print("True")
    else:
        print("False")   