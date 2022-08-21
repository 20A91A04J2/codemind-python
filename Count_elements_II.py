a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
f=[]
for i in c:
    if i not in e:
        e.append(i)
for j in d:
    if j not in f:
        f.append(j)
count=0
for k in e:
    if k not in f:
        count=count+1
for m in f:
    if m not in e:
        count=count+1
print(count)