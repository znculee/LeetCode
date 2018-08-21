# 80. Remove Duplicates from Sorted Array II

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        i = 0
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        return i


def test():
    s = Solution()

    nums = [1]
    length = s.removeDuplicates(nums)
    print(f'{nums=}\n{length=}\n')

    nums = [1,2]
    length = s.removeDuplicates(nums)
    print(f'{nums=}\n{length=}\n')

    nums = [1,1,1,2,2,3]
    length = s.removeDuplicates(nums)
    print(f'{nums=}\n{length=}\n')

    nums = [0,0,1,1,1,1,2,3,3]
    length = s.removeDuplicates(nums)
    print(f'{nums=}\n{length=}')


if __name__ == '__main__':
    test()
