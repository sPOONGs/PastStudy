num = int(input("숫자를 입력 하세요 :"))

for i in range(num):
    if( i % 2 == 0):
        continue
    elif( i % 3 == 0):
        continue
    print("현재 i 값",i)

print("반복문 종료")
