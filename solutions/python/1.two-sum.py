# 1. Two Sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            if nums[i] not in diff:
                diff[target-nums[i]] = i
            else:
                return diff[nums[i]], i


def test():
    s = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    result = s.twoSum(nums, target)
    print(f'{nums=}\n{target=}\n{result=}')


if __name__ == '__main__':
    test()
