import sys
N = int(input())
s = []
for  i in range(N):
    s.append(sys.stdin.readline().rstrip())
sol = list(set(s))
sol.sort(key=lambda x:(len(x),x))
for char in sol:
    print(char)