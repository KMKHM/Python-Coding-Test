from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraphList = []
        for nobanned in paragraph.split():
            if nobanned != banned[0]:
                paragraphList.append(nobanned.lower())
        return paragraphList

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." 
banned = ["hit"]
sol = Solution()
print(sol.mostCommonWord(paragraph, banned))