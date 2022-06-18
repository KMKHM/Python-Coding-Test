from typing import List

class MySolution:
    def reverseString(self, s: List[str]) -> None:
        a = s.reverse() 

# Two Pointer
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left +=1
            right -=1  