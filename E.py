from re import A


dict1={}
while 1:
    try:
        a,b=input().split()
        dict1[b]=a
    except:
        break
while 1:
    try:
        a=input()
        if a in dict1:

            print(dict1[a])
        else:
            print("eh")
    except:
        break