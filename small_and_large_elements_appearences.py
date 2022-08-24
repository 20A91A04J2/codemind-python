a=str(input())
b=list(a)
c=[]
for i in range(len(b)):
    if(b[i]!=" "):
        c.append(b[i])
d=min(c)
e=c.count(d)
f=max(c)
g=c.count(f)
print(d,e,f,g)