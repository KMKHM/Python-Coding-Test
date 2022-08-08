n , k = map(int, input.split())

def solution(n, k):
    answer_list = []
    for i in range(1,n+1):
        if n % i == 0:
            answer_list.append(i)
    if len(answer_list) < k:
        return -1
    else:
        return answer_list[k-1]

print(solution(n,k))