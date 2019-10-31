def getPrime(n):
    arr = []
    for i in range(2,int(n**0.5)+2):
        while n%i == 0:
            arr.append(i)
            n = n/i
    if n>1: arr.append(int(n))
    for i in arr:
        print(i,end=' ')

while True:
    try:
        n = int(input())
        getPrime(n)
    except:
        break


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