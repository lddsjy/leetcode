# n = input().strip()
# for i in range(n):
#     s = input().strip()
#     s0 = s[-1]
#     s0 = chr(ord(s0.lower())-32)
#     s = s[:-1]+s0
#     print(s)

temp = input().strip().split()
l,t = [int(i) for i in temp]
s = input().strip().split()
for i in range(t):
    left,right = [int(k) for k in input().strip().split()]
    for j in range(left-1,right):
        print(s,j)
        if s[j]=='1':
            s[j] ='0'
        else:
            s[j] = '1'
print(s)