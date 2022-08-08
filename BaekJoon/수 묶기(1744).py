N = int(input())

positive_list  = [] 
negative_list = [] 
sol = 0
for _ in range(N):
  n = int(input())
  if n > 1:
    positive_list.append(n)
  elif n == 1:
    sol += 1 
  else:
    negative_list.append(n)

positive_list.sort(reverse=True) 
negative_list.sort() 

# 양수부분
if len(positive_list) % 2 == 0: 
  for i in range(0, len(positive_list), 2):
    sol += positive_list[i] * positive_list[i+1]
else:
  for i in range(0, len(positive_list)-1, 2): 
    sol += positive_list[i] * positive_list[i+1]
  sol += positive_list[len(positive_list)-1] 

# 음수부분
if len(negative_list) % 2 == 0: # 음수가 짝수개 일경우 두개씩 곱해준다.
  for i in range(0, len(negative_list), 2):
    sol += negative_list[i] * negative_list[i+1]
else:
  for i in range(0, len(negative_list)-1, 2):
    sol += negative_list[i] * negative_list[i+1]
  sol += negative_list[len(negative_list)-1] # 마지막 수는 더해준다.

print(sol)