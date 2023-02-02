N = int(input())

for i in range (N) :
    A , B = map(int, input().split()) # A>0, B<10
    
    print("Case #%d: %d" %((i+1), (A+B)))
    
