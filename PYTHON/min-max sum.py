arr = list(map(int, input().split()))
sum=0
for i in range(len(arr)):
    sum+=arr[i]
print (sum-max(arr), sum-min(arr))