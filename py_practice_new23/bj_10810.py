N , M = map(int, input().split()) #바구니 N개 입력 M번

pocket = [ 0 for i in range(N)] # 입력한 N 개수의 바구니 

for m in range(M):
    ball_info = list(map(int, input().split())) # 1 2 3 

    for i in range ((ball_info[0]-1),ball_info[1]):
        pocket[i] = ball_info[2]


print(*pocket)