n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    if(i%2==0):
        b=int(a[i+1])
        for j in range(b):
            c.append(a[i])
print(*c)