n = input()
arr = int(input())
l = len(n)
nos = arr//l
rem = arr%l

c1 = 0
c2 = 0
for i in range(l):
    if n[i] == 'a':
        c1+=1
    if n[i] == 'a' and i < rem:
        c2+=1
sum = (c1*nos)+c2
print(sum)