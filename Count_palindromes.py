n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(len(a)):
    b=str(a[i])
    c=list(b)
    d=c[::-1]
    count=0
    for j in range(len(d)):
        if(c[j]==d[j]):
            count=count+1
    if(count==int(len(c))):
        sum=sum+1
print(sum)