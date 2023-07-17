from typing import *
def rotate(nums:List[int], k: int) -> None:
    i=0
    while i<k:
        var = nums.pop(-1)
        nums.insert(0, var)
        i+=1
    return nums
nums = [-1,-100,3,99]
print(rotate(nums, 5))