class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not p:
            return False
        # if len(p) == 1:
        #     if len(s)==1 and (s==p or p=='.'):
        #         return True
        #     else:
        #         return False
        if len(p)>1 and p[1] == '*':
            if s and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:],p[2:]) or self.isMatch(s[1:],p) or self.isMatch(s,p[2:])
            else:
                return self.isMatch(s,p[2:])
        else:
            if s and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:],p[1:])
            else:
                return False
s = Solution()
print(s.isMatch('aa','a'))
print(s.isMatch('aa','a*'))
print(s.isMatch('ab','.*'))
print(s.isMatch('aab','c*a*b'))
print(s.isMatch('mississippi','mis*is*p*.'))
print(s.isMatch('ab','.*c'))
print(s.isMatch('a','ab*'))