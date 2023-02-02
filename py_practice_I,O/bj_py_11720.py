N = int(input())
nums = list(map(int, input()))
result = 0


for i in range (N):
   result += nums[i]

print(result)