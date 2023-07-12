N , M = map(int, input().split())

basket = [ (i+1) for i in range(N)]
for m in range(M):
    i, j = list(map(int, input().split()))
    after_basket = list(reversed(basket[(i-1) : j])) #reversed 에 있는 
    basket[(i-1) : j] = after_basket
    
print(*basket)
