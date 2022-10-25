n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i<n:
        c+=1
if c==n:
    print("YES")
else:
    print("NO")