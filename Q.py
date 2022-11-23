while 1:
    try:
        input()
        list1=[int(i) for i in input().split()]
        list1.sort()
        t=0
        while len(list1)>1:
            a=list1[0]
            del list1[0]
            b=list1[0]
            t+=a+b
            del list1[0]
            list1.append(a+b)
            list1.sort()

        print(t)
    except:
        break