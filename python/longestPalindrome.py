class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #必须加self
        self.longest=''
        def check(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i = i-1
                j = j+1
            #倒数第二轮改变的i,j值是通过值
            if len(s[i+1:j]) > len(self.longest):
                self.longest = s[i+1:j]

        for i in range(len(s)):
            check(i,i)
            check(i,i+1)
        return self.longest

s = Solution()
print(s.longestPalindrome('cbbd'))