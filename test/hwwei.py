thr = input().strip().split(']')
print(thr)
d = {}
for i in thr[:-1]:
    if i[0] == ',':
        i = i[1:]
    d[int(i[0])] = [int(j) for j in i[3:].split(',')]
print(d)
order= sorted(d)
for i in order:
    for j in d[i]:
