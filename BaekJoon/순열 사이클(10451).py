from collections import deque
list1 = [3,2,7,8,1,4,5,6]
list2 = sorted(list1)
n = len(list1)
cnt = 0
for i in range(n):
    if list1[i] == list2[i]:
        cnt +=1
    else:
        q = deque()
        
