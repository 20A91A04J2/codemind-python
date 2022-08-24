a=str(input())
b=a.split()
for i in range(len(b)):
    c=min(b[i])
    d=max(b[i])
    print(c,d,end=" ")