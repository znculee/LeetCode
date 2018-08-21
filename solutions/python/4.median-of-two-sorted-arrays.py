# 4. Median of Two Sorted Arrays

import sys
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(nums1:List[int], i:int, nums2:List[int], j:int, k:int) -> float:
            if i >= len(nums1): return nums2[j+k-1]
            if j >= len(nums2): return nums1[i+k-1]
            if k == 1: return min(nums1[i], nums2[j])
            if i + k // 2 - 1 < len(nums1):
                midval1 = nums1[i+k//2-1]
            else:
                midval1 = sys.maxsize
            if j + k // 2 - 1 < len(nums2):
                midval2 = nums2[j+k//2-1]
            else:
                midval2 = sys.maxint
            if midval1 < midval2:
                return findKth(nums1, i+k//2, nums2, j, k-k//2)
            else:
                return findKth(nums1, i, nums2, j+k//2, k-k//2)
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        return (findKth(nums1, 0, nums2, 0, left) +
            findKth(nums1, 0, nums2, 0, right)) // 2.0


def test():
    s = Solution()

    nums1 = [1, 3]
    nums2 = [2]
    output = s.findMedianSortedArrays(nums1, nums2)
    print(f'{nums1=}\n{nums2=}\n{output=}\n')

    nums1 = [1, 2]
    nums2 = [3, 4]
    output = s.findMedianSortedArrays(nums1, nums2)
    print(f'{nums1=}\n{nums2=}\n{output=}\n')

    nums1 = [1]
    nums2 = [2, 3, 4, 5, 6]
    output = s.findMedianSortedArrays(nums1, nums2)
    print(f'{nums1=}\n{nums2=}\n{output=}')


if __name__ == '__main__':
    test()
