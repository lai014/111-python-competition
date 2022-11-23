for _ in range(int(input())):
    a=input()
    if len(a)==5:
        print(3)
    else:
        if ("t"==a[0] and "w"==a[1]) or ("w"==a[1] and a[2]=="o") or("t"==a[0] and "o"==a[2]):
            print(2)
        else:
            print(1)