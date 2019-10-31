inp = input().strip().split(';')
arr_out =[]
print('r'.value)
for strs in inp:
    arr = []
    #print('a'-'A')
    for i in strs:
        if i>'A' and i <'z':
            arr.append(i)
        else:
            break
    print(arr)
    arr_out.append(abs(ascii(arr[0])-ascii(arr[-1])))
print(sum(arr_out))



# day = int(input())
#
# if day < 1:
#     print('error')
# else:
#     arr = [3]
# for i in range(1,day):
#     arr.append(i*3)
# h = 0
# while arr:
#     h = (h+arr.pop())*2
# print(h)