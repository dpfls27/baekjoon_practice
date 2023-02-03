N = int(input())

temp = list(map(int, input().split()))

max = temp[0]
min = temp[0]

for i in range (N):
    if temp[i]>max:
        max = temp[i]
        
    elif temp[i]<min:
        min = temp[i]

print(min, max)