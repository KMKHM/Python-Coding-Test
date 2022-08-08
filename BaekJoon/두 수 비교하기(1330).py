a, b = map(int, input().split())
def solution(a,b):
    if a>b: return ">"
    elif a<b: return "<"
    else: return "=="

print(solution(a,b))