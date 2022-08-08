from typing import List

class MySolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

# in을 이용한 탐색
nums = [2,7,11,15]
target = 9
def two(nums, target):
    return
