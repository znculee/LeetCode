# 81. Search in Rotated Sorted Array II

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return True
            if nums[mid] < nums[right]:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[right]:
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right -= 1
        return False


def test():
    s = Solution()

    nums = [2,5,6,0,0,1,2]
    target = 0
    output = s.search(nums, target)
    print(f'{nums=}\n{target=}\n{output=}\n')

    nums = [2,5,6,0,0,1,2]
    target = 3
    output = s.search(nums, target)
    print(f'{nums=}\n{target=}\n{output=}')


if __name__ == '__main__':
    test()
