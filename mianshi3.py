
n, m = list(map(int, input().split()))
lst = list(map(int, input().split()))
out = [0]*n
for i in range(len(lst)):
    out[lst[i]-1] += 1
print(min(out))
