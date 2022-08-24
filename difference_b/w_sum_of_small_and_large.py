a=str(input())
b=a.split()
c=[]
d=[]
for i in range(len(b)):
    c.append(min(b[i]))
    d.append(max(b[i]))
sum=0
count=0
for j in range(len(c)):
    sum=sum+int(ord(c[j]))
    count=count+int(ord(d[j]))
print(abs(sum-count))