n=int(input())
a=list(map(int,input().split()))
f=[]
for i in range(len(a)):
    b=int(a[i])
    c=b
    re=0
    while(c!=0):
        r=c%10
        re=(re*10)+r
        c=c//10
    f.append(re)
print(*f)