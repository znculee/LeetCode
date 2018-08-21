# 26. Remove Duplicates from Sorted Array

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        pre = 0
        for cur, num in enumerate(nums):
            if nums[cur] != nums[pre]:
                pre += 1
                nums[pre] = nums[cur]
        del nums[pre+1:]
        return (pre+1)

def test():
    s = Solution()

    nums = [1,1,2]
    length = s.removeDuplicates(nums)
    print(f'{nums=}\n{length=}\n')

    nums = [0,0,1,1,1,2,2,3,3,4]
    length = s.removeDuplicates(nums)
    print(f'{nums=}\n{length=}')


if __name__ == '__main__':
    test()
