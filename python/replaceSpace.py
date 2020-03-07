# -*- coding:utf-8 -*-
#无法计数空格
# class Solution:
#     # s 源字符串
#     def replaceSpace(self, s):
#         arr = s.split()
#         return "%20".join(arr)

class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')

# class Solution:
#     # s 源字符串
#     def replaceSpace(self, s):
#         # write code here
#         print(list(s))
#         pos = []
#         s = list(s)
#         for i in range(len(s)):
#             if s[i] == ' ':
#                 s[i] = '%20'
#                 #s= s[:i]+'%20'+ remain
#         news = ''
#         for i in range(len(s)):
#             news += s[i]
#         return news

s = Solution()
print(s.replaceSpace("   "))
