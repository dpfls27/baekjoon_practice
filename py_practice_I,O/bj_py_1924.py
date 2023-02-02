x, y = map(int, input().split()) #m은 월, y는 일
days = ['SUN','MON', 'TUE', 'WED','THU', 'FRI', 'SAT']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d = 0

for i in range(0, x-1):
    d += month[i]
    

d = (d+y)%7 #d에 y변수인 일까지 다 더한 후 7로 나눈 나머지로 요일을 알 수 있음

print(days[d])