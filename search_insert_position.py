from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            nums.append(target)
            nums.sort()
            return nums.index(target)