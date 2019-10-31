# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if len(s)==0 and len(pattern)==0:
            return True
        if len(s)!=0 and len(pattern)==0:
            return False
        if len(s)==0 and len(pattern)!=0:
            if len(pattern)>1 and pattern[1]=='*':
                return self.match(s,pattern[2:])
            else:
                return False
        elif len(pattern)>1 and pattern[1]=='*':
            if s[0] == pattern[0] or pattern[0]=='.':
                return self.match(s[1:],pattern) or self.match(s[1:],pattern[2:]) or self.match(s,pattern[2:])
            else:
                return self.match(s,pattern[2:])
        elif s[0] == pattern[0] or pattern[0]=='.':
            return self.match(s[1:],pattern[1:])
        else:
            return False

s = Solution()
print(s.match('aaa','ab*ac*a'))
print(s.match('aaa','a.a'))
print(s.match('aaa','aa.a'))
print(s.match('aaa','ab*a'))
print(s.match('aa','a*'))
print(s.match('aa','.*'))
print(s.match('bbbba','.*a*a'))
