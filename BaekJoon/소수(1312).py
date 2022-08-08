#a,b,n = map(int, input().split())
def solution(a,b,n):
    return str(a/b)[n+1]

#print(solution(a,b,n))
print(solution(3,4,1))
print(3/4)