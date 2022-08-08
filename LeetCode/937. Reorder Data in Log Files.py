from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig = []
        let = []
        for a in logs:
            if a.split(" ")[1].isdigit():
                dig.append(a)
            else:
                let.append(a)
        let.sort(key = lambda x: (x.split()[1:], x.split()[0])) # 람다 표현식 다시 공부         
        return let+dig

