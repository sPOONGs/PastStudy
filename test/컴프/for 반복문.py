print("숫자를 키보드로 입력 받고 , 홀수면 출력")
print("짝수면 누적 시켜 총합을 구하는 예제")

number = int(input("숫자를 입력하시오. :"))
sum = 0

for i in range(number):
    if(i%2==0):
        sum += i

    else:
        print(i, "현재 값 홀수")

print("\n반복문 끝")
print("입력 받은 수의 0부터 짝수의 총합 :",sum)
