N , M = map(int, input().split())

basket = [ (i+1) for i in range(N)]

for m in range(M):
    num1, num2 = list(map(int, input().split()))
    basket[num1-1] , basket[num2 -1] = basket[num2 -1] , basket[num1-1]

print(*basket)