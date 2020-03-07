#q j
while True:
    try:
        arr = [i for i in input().strip().split(',')]
        arr_new = sorted(arr)
        print(' '.join(arr_new))
    except:
        break

#q i
while True:
    try:
        arr = [i for i in input().strip().split()]
        arr_new = sorted(arr)
        for i in arr_new:
            print(i,end=' ')
        print()#若是\n会出现两个换行
    except:
        break

#q h:********
num = int(input())
arr = [i for i in input().strip().split()]
arr_new = sorted(arr)
for i in arr_new:
    print(i,end=' ')
#qd
import sys
for line in sys.stdin:
    arr = [int(i) for i in line.strip().split()[1:]]
    if arr[0] == 0 and len(arr) == 1:
        break
    else:
        print(sum(arr))

#q3
while True:
    try:
        arr = [int(i) for i in input().strip().split()]
        if arr[0] == 0 and arr[1] == 0:
            break
        else:
            print(sum(arr))
    except:
        break
#q2
# num = int(input())
# for i in range(num):
#     list1 = [int(j) for j in input().strip().split()]
#     print(sum(list1))

#q1
# while True:
#     try:
#         arr = [int(i) for i in input().strip().split()]
#         print(sum(arr))
#     except:
#         break