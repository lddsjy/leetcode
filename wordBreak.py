class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [0]*(len(s)+1)
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if i>0 and dp[i] != 1:
                    break
                if s[i:j] in wordDict:
                    dp[j] = 1
        print(dp)
        if dp[len(s)]:
            return True
        return False

s = Solution()
print(s.wordBreak("leetcode",
["leet","code"]))