N = int(input())
grade = list(map(int, input().split()))

M  = max(grade)
for n in range(N):
    grade[n] = grade[n]/M*100
    
average = sum(grade)/len(grade)
print(average)