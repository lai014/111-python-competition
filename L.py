while 1:
    try:
        a,b=map(int,input().split())
        list1=[1]

        for i in range(2,a+1):
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                list1.append(i)
        t=len(list1)//2
        g=0
        if len(list1)%2==0:
            g=2*b
        else:
            g=2*b+1
        print("%d %d: "%(a,b),end="")
        if g>len(list1):
            print(*list1)

        else:
            list10=[]
            if g%2==0:
                list10.append(list1[t])
                for i in range(t-1,t-b-1,-1):
                    list10.append(list1[i])
                for i in range(t+1,t+b):
                    list10.append(list1[i])
            else:
                list10.append(list1[t])
                for i in range(t-1,t-b,-1):
                    list10.append(list1[i])
                for i in range(t+1,t+b):
                    list10.append(list1[i])
            list10.sort()
            print(*list10)
    except:
        break