a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if(i%2!=0):
        count=count+1
for j in range(a,b):
    for k in range(j+1,b+1):
        c=int(j+k)
        if(c%2!=0):
            count=count+1
print(count)