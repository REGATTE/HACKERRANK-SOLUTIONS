def difference(arr, n): 
    d1 = 0
    d2 = 0
  
    for i in range(0, n): 
        d1 = d1 + arr[i][i] 
        d2 = d2 + arr[i][n - i - 1] 
 
    return abs(d1 - d2) 

n = int(input())
arr = []
for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

print(difference(arr, n))