import collections
import re
from typing import Deque

class MySolution:
    def isPalindrome(self, s: str) -> bool:
        sList = []
        for i in s:
            if i.isalnum(): 
                sList.append(i.lower()) 
        return sList == sList[::-1]

# While문 사용
class OtherSolution1:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): 
                strs.append(char.lower()) 
        
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

class OtherSolution2:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

class OtherSolution3:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # re.sub('찾을 패턴', '찾은 패턴을 변경할 내용', '원본')
        s = re.sub("[^a-z0-9]", "",s) 
        return s == s[::-1]