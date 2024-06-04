while True:
    num = int(input("0~100 사이의 값을 입력 하세요 : "))

    if(num == 0):
        print(" 0값이 입력! \n프로그램 종료")
        break

    elif(0 < num <= 100):
        print("입력값: ",num)

    else:
        print("범위를 벗어났습니다. 다시 입력하세요")

    
