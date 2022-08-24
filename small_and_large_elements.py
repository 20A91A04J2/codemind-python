a=str(input())
b=a.split()
for i in range(len(b)):
    c=min(b[0])
    d=max(b[len(b)-1])
    print(c,d)
    break