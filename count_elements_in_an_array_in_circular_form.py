n=int(input())
a=list(map(int,input().split()))
count=0
j=0
k=0
for i in range(n):
    if(a[i]%2==0):
        j=i+2
        if(j<n):
            if(a[j]%2!=0):
                count=count+1
    else:
        k=i+2
        if(k<n):
            if(a[k]%2==0):
                count=count+1
if(int(a[n-2])%2==0 and int(a[0])%2!=0):
    count=count+1
elif(int(a[n-2])%2!=0 and int(a[0])%2==0):
    count=count+1
elif(int(a[n-1])%2!=0 and int(a[1])%2==0):
    count=count+1
elif(int(a[n-1])%2==0 and int(a[1])%2!=0):
    count=count+1
print(count)