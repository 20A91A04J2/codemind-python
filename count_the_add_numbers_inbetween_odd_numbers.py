n=int(input())
a=list(map(int,input().split()))
count=0
j=0
for i in range(n):
    if(a[i]%2!=0):
        j=i+2
        if(j<n):
            if(a[j]%2!=0):
                if(a[j-1]%2!=0):
                    count=count+1
print(count)
                