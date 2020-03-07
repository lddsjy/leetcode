while True:
    try:
        n = int(input())
        d= {}
        for i in range(n):
            k,v = map(int,input().split())
            d[k] = d.setdefault(k,0)+v
        print(sorted(d,key=d.values()))
        for k in sorted(d.keys()):
            print(k,d[k])
    except:
        break
