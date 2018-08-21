# 5. Longest Palindromic Substring

# Dynamic Programming
class Solution_dp:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        l = len(s)
        if l == 1 or l == 0: return s
        if l == 2:
            if s[0] == s[1]: return s
            else: return s[0]
        dp = [None] * l
        if s[0] == s[1]:
            dp[:2] = [True] * 2
            longest = 2
            ip, jp = 1, 0
        else:
            dp[0], dp[1] = False, True
            longest = 1
            ip, jp = 0, 0
        for i in range(2, l):
            for j in range(i+1):
                if i - j > 1:
                    dp[j] = s[j] == s[i] and dp[j+1]
                    if dp[j]:
                        palindromic = i - j + 1
                        if longest < palindromic:
                            longest = palindromic
                            ip, jp = i, j
                if i - j == 1:
                    dp[j] = s[j] == s[i]
                    if longest < 2 and dp[j]:
                        longest = 2
                        ip, jp = i, j
                if i - j == 0:
                    dp[j] = True
        return s[jp:ip+1]


# Palindromic Substring Equals Its Reverse
class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2 or s==s[::-1]:
            return s
        n=len(s)
        start,maxlen=0,1
        for i in range(n):
            odd =s[i-maxlen-1:i+1]
            even=s[i-maxlen:i+1]
            if i-maxlen-1>=0 and odd==odd[::-1]:
                start=i-maxlen-1
                maxlen+=2
                continue
            if i-maxlen>=0 and even==even[::-1]:
                start=i-maxlen
                maxlen+=1
        return s[start:start+maxlen]


def test():
    s = Solution()

    string = "babad"
    output = s.longestPalindrome(string)
    print(f'{string=}\n{output=}\n')

    string = "cbbd"
    output = s.longestPalindrome(string)
    print(f'{string=}\n{output=}\n')

    string = ""
    output = s.longestPalindrome(string)
    print(f'{string=}\n{output=}\n')

    string = "ccc"
    output = s.longestPalindrome(string)
    print(f'{string=}\n{output=}\n')

    string = "ccd"
    output = s.longestPalindrome(string)
    print(f'{string=}\n{output=}\n')

    string = "caba"
    output = s.longestPalindrome(string)
    print(f'{string=}\n{output=}')


if __name__ == '__main__':
    test()
