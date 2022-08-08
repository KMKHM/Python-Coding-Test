import math
M = 60
N = 100
nums = []
for num in range(M,N+1):
    if (str(math.sqrt(num))[2]=="0" and len(str(math.sqrt(num)))==3):
        nums.append(num)
print(num)

