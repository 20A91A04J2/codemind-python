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
e=[]
for k in range(len(d)):
    if(int(d[k])==int(b[k])):
        e.append(b[k])
if(len(e)!=0):
    f=sum(e)
    g=(f/int(len(e)))
    print("{:.2f}".format(g))
else:
    print("-1")