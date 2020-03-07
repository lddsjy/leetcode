num = int(input())
arr = []
for i in range(num):
    s = int(input().strip())
    if s not in arr:
        arr.append(s)
arr = sorted(arr)
for i in arr:
    print(i)