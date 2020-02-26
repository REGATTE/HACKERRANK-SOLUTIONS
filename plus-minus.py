n = int(input())
arr = list(map(int, input().split()))
a=0
b=0
c=0
for i in range(len(arr)):
    if(arr[i]>0):
        a+=1
    if(arr[i]<0):
        b+=1
    if(arr[i]==0):
        c+=1
print(a/n)
print(b/n)
print(c/n)