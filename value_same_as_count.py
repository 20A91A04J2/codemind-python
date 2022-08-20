n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
d=[]
for j in range(len(b)):
    c=a.count(b[j])
    d.append(c)
count=0
for k in range(len(d)):
    if(int(d[k])==int(b[k])):
        count=count+1
print(count)