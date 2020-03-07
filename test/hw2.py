# while True:
#     try:
cnt = 0
s= set(input())
for i in s:
    if 0<=ord(i)<=127:
        cnt += 1
print(cnt)
    # except:
    #     break
# while True:
#     try:
#         n = input().strip()
#         s =  list(str(n))
#         str = ''
#         while s:
#             i = s.pop()
#             #print(i)
#             if not i in str:
#                 str+=i
#
#         print(int(str))
#         #print(''.join(str))
#     except:
#         break

# def getPrime(n):
#     arr = []
#     for i in range(2,int(n**0.5)+2):
#         while n%i == 0:
#             arr.append(i)
#             n = n/i
#     if n>1: arr.append(int(n))
#     for i in arr:
#         print(i,end=' ')

# while True:
#     try:
#         n = int(input())
#         getPrime(n)
#     except:
#         break


# a=int(input())
# def qiuzhishu(x):
#     iszhi=1
#     for i in range(2,int(x**0.5+2)):
#         if x%i==0:
#             iszhi=0
#             print(str(i),end=" ")
#             qiuzhishu(int(x/i))
#             break
#     if iszhi==1:
#         print(str(x),end=" ")
# qiuzhishu(a)