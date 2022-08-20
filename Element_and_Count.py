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
e=[]
for k in range(len(b)):
    e.append(b[k])
    e.append(d[k])
print(*e)