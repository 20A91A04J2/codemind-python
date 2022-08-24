a=str(input())
b=a.split()
c=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in range(len(b)):
    for j in range(len(b[i])):
        d=b[i]
        e=d[::-1]
        for k in range(len(e)):
            if d[k] not in c:
                if e[k] in c:
                    count=count+1
        break
print(count)