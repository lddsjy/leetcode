# -*- coding:utf-8 -*-
#辅助栈
class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV and popV:
            realPop = []
            # id = pushV.index(popV[0])
            # for i in range(id+1):
            #     realPop.append(pushV[0])
            #     pushV.pop(0)
            # popV.pop(0)
            # realPop.pop(-1)
            while popV:
                print(pushV,popV,realPop)
                if realPop and popV[0] == realPop[-1]:
                    popV.pop(0)
                    realPop.pop(-1)
                elif pushV and popV[0] in pushV:
                    id = pushV.index(popV[0])
                    for i in range(id + 1):
                        realPop.append(pushV[0])
                        pushV.pop(0)
                    popV.pop(0)
                    realPop.pop(-1)
                else:
                    return False
            return True


s = Solution()
print(s.IsPopOrder([1,2,3,4,5],[3,5,4,1,2]))
