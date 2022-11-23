a=int(input())
for i in range(a):
    t=int(input())
    if t%4==0 and t%100!=0 or t%400==0:
        print("a leap year")
    else:
        print("a normal year")
