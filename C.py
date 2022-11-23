while 1:
    try:
        a=input()
        t=int(a[0])
        s=0
        for i in a[1:]:
            if s%2==0:
                t+=int(i)
            else:
                t-=int(i)
            s+=1
        print(t)
    except:
        break