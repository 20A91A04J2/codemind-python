a=str(input())
c=['a','e','i','o','u','A','E','I','O','U']
d=a[::-1]
count=0
for j in range(len(d)):
    if a[j] not in c and a[j]!=" ":
        if d[j] in c:
            count=count+1
print(count)