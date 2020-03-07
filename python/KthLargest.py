import heapq
class KthLargest:
    def __init__(self,k:int,nums):
        self.pool = heapq.nlargest(k,nums)
        heapq.heapify(self.pool)
        self.k=k
        print(self.pool)
    def add(self,val:int):
        if len(self.pool)<self.k:
            heapq.heappush(self.pool,val)
        else:
            heapq.heappushpop(self.pool,val)
            print(self.pool)
        return self.pool[0]

s = KthLargest(3,[4,5,8,2])
s.add(3)
s.add(5)

