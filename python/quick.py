def quick_sort(data):
    if len(data)>1:
        mid = data[len(data)//2]
        left,right = [],[]
        data = data[:len(data)//2]+data[len(data)//2+1:]
        #         data.remove(mid)    从原始数组中移除基准值
        for i in data:
            if i<mid:
                left.append(i)
            else:
                right.append(i)
        left = quick_sort(left)
        right = quick_sort(right)
        return left+[mid]+right
    else:
        return data

def insert_sort(data):
    if len(data)>1:
        for i in range(1,len(data)):
            tmp = data[i]
            j = i-1
            while j>=0 and tmp<data[j]:
                data[j+1] = data[j]
                j = j-1
            data[j+1]=tmp
    return data
def merge(left,right):
    arr = []
    i,j = 0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr.append(left[i])
            i = i+1
        else:
            arr.append(right[j])
            j = j+1
    arr.extend(left[i:])
    arr.extend(right[j:])
    return arr
def merge_sort(data):
    if len(data)<=1:
        return data
    mid = len(data)//2
    left = data[:mid]
    right = data[mid:]
    return merge(left,right)


array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(len(array))
print(quick_sort(array))
print(insert_sort(array))
print(merge_sort(array))