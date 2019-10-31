# print(sorted(['a','c','b']))
# print(sorted('acdbjg'))
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        if len(ss) == 1:
            return ss
        upss = sorted(ss)
        ret= []
        for i in range(len(upss)):
            rest = upss[:i]+upss[i+1:]
            restMutation = self.Permutation(rest)
            #print(restMutation)
            for j in range(len(restMutation)):
                tmp = upss[i]+restMutation[j]
                #if not ret or (ret and tmp != ret[-1]):
                ret.append(tmp)
            #print(ret)
        ret = list(sorted(set(ret)))
        return ret
# class Solution:
#     def Permutation(self, ss):
#         if not ss:
#             return []
#         if len(ss) == 1:
#             return [ss]
#         upss = sorted(ss)
#         ret= []
#         for i in range(len(upss)):
#             rest = upss[:i]+upss[i+1:]
#             restMutation = self.Permutation(rest)
#             #print(restMutation)
#             for j in range(len(restMutation)):
#                 if not ret or (ret and ([upss[i]]+restMutation[j]) != ret[-1]):
#                     ret.append([upss[i]]+restMutation[j])
#             #print(ret)
#         return ret

s = Solution()
print(s.Permutation('abc'))
