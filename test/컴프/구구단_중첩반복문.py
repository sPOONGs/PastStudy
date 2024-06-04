num = int(input("몇단 까지 출력 할까요? : "))

for i in range(1, num + 1):
    for j in range(1,10):
        print("%d x %d = %d"%(i , j , i * j))

    print()

print("입력받은 구구단 출력 끝")


name = "홍길동"
age = 22
length = 183.5

print("나의 이름은 %s, 나이는 %d , 키는 %0.1lf cm입니다."%(name , age , length))


