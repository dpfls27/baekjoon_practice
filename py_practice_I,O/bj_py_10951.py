while 1: #입력값의 개수를 주지 않을때 쓰는 try~except로 
    try: 
        A , B = map(int, input().split()) 

    except:
        break
    print(A+B)

#그냥 while문 속에 if문을 쓰면 EOF에러남 그래서 try~except로 예외처리를 해줘야함.