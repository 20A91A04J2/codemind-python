n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(len(a)):
    j=i+2
    if(j<n-1):
        if(int(a[i])+int(a[j-1])==int(a[j])):
            count=count+1
        else:
            count=count+0
if(count==int(n-3)):
    print("yes")
else:
    print("no")