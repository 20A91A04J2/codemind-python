n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(len(a)):
    b=int(a[i])
    c=b
    while(c!=0):
        r=c%10
        sum=sum+r
        c=c//10
print(sum)