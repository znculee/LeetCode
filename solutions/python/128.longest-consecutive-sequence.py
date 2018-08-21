# 128. Longest Consecutive Sequence

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)
        for val in nums:
            if val not in s:
                continue
            s.remove(val)
            pre = val - 1
            next_ = val + 1
            while pre in s:
                s.remove(pre)
                pre -= 1
            while next_ in s:
                s.remove(next_)
                next_ += 1
            res = max(res, next_ - pre - 1)
        return res


def test():
    s = Solution()

    input_ = [100, 4, 200, 1, 3, 2]
    output = s.longestConsecutive(input_)
    print(f'{input_=}\n{output=}')


if __name__ == '__main__':
    test()
