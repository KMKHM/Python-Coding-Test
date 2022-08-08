T = int(input())

for _ in range(T):
    N = int(input())
    result = 0

    queue = list(map(int, input().split()))
    
    while True:
        if len(queue)==0:
            break
        
        num = queue.pop()

        for i in range(len(queue)-1,-1,-1):
            if num >= queue[i]:
                result += (num - queue[i])
                queue.pop()
            else: 
                break
    

    print(result)