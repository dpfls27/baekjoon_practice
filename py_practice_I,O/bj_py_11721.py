Words = input() #문자열은 문자의 배열형태기 때문에 이렇게 받아서 바로 출력 가능

l = len(Words)

for i in range(0, l ,10):
    # print(''.join(Words[i:i+10])) 얘는 리스트 요소만 출력하고 싶을때 쓰는 방법
    # print(*Words[i:i+10]) 얘는 포인터로 해서 리스트 요소만 출력 근데 요소마다 빈칸 생기는 단점
    print(Words[i:i+10])

    
