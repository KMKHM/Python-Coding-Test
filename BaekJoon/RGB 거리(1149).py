N = int(input())
sol = []

for i in range(N):
    sol.append(list(map(int, input().split())))

for i in range(1, len(sol)):
    sol[i][0] = min(sol[i - 1][1], sol[i - 1][2]) + sol[i][0]
    sol[i][1] = min(sol[i - 1][0], sol[i - 1][2]) + sol[i][1]
    sol[i][2] = min(sol[i - 1][0], sol[i - 1][1]) + sol[i][2]

print(min(sol[N - 1][0], sol[N - 1][1], sol[N - 1][2]))