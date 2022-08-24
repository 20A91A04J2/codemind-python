a=str(input())
b=a.split()
c=[]
for i in range(len(b)):
    sum=0
    for j in range(len(b[i])):
        d=b[i]
        sum=sum+ord(d[j])
    c.append(sum)
d=sorted(c)
e=[]
for j in range(len(d)):
    for k in range(len(c)):
        if(d[j]==c[k]):
            e.append(b[k])
print(*e)
