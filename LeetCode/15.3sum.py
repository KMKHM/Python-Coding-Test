from typing import List

# 시간 초과 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp_answer = [nums[i],nums[j],nums[k]]
                        temp_answer.sort()
                        if temp_answer not in answer:
                            answer.append(temp_answer)
        return answer

