from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list) # 다시 공부

        for elem in strs: 
            dict["".join(sorted(elem))].append(elem)
        return list(dict.values())

