for _ in range(int(input())):
    list1=[]
    t=input().split()
    for i in range(0,20,2):
        list1.append(t[i]+t[i+1])
    r=0
    for i in list1:
        r+=int(i,16)
    ans=hex(r)[2:]
    ans1=hex(int(ans[-4:],16)+int(ans[:-4],16))[2:]
    ans2=(bin((int(ans1,16))))[2:]
    ans2=ans2.rjust(16,"0")
    ans3=""
    for i in ans2:
        if i=="0":
            ans3+="1"
        else:
            ans3+="0"
    ans3=ans3.rjust(16,"0")
    ans3=hex(int(ans3,2))[2:]
    ans3=ans3.rjust(4,"0")
    print(ans3)