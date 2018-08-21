# 903. Valid Permutations for DI Sequence

class Solution:
    def numPermsDISequence(self, S: str) -> int:
        n = len(S)
        M = 1e9 + 7
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            dp_ = [0] * (n+1)
            for j in range(i+1):
                if S[i-1] == 'D':
                    for k in range(j, i):
                        dp_[j] = (dp_[j] + dp[k]) % M
                else:
                    for k in range(j):
                        dp_[j] = (dp_[j] + dp[k]) % M
            dp = dp_
        res = int(sum(dp) % M)

        return res


def test():
    s = Solution()

    seq = "DID"
    output = s.numPermsDISequence(seq)
    print(f'{seq=}\n{output=}')


if __name__ == '__main__':
    test()
