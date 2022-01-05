#1 학점 출력 프로그램
# SWITCH문을 if와 elif로 구현
def get_credits(SCORE):
    if SCORE > 95 and SCORE <= 100:
        print('A+')
    elif SCORE > 90 and SCORE < 96:
        print('A')
    elif SCORE > 85 and SCORE < 91:
        print('B+')
    elif SCORE > 80 and SCORE < 86:
        print('B')
    elif SCORE > 75 and SCORE < 81:
        print('C+')
    elif SCORE > 70 and SCORE < 76:
        print('C')
    elif SCORE > 65 and SCORE < 71:
        print('D+')
    elif SCORE > 60 and SCORE < 66:
        print('D')
    elif SCORE > 0 and SCORE < 61:
        print('F')
    else:
        print('입력값이 올바르지 않습니다.')

#2 시, 분, 초 변환기
# 1시간 -> 3600초, 1분 -> 60초 알고리즘 적용 및 구현
# 입력받는 매개변수가 숫자라고 가정한 함수
def time_converter(SEC):
    hour = SEC // 3600
    minuate = (SEC % 3600) // 60
    sec = (SEC % 3600) % 60
    print('{}시간 {}분 {}초'.format(hour, minuate, sec))

# 입력받는 매개변수가 숫자가 아닐 경우를 포함한 함수
def time_converter2(SEC):
    if type(SEC) == int and SEC >= 0: # 입력받은 매개변수의 타입이 정수형이고, 0보다 크거나 같을 때 실행
        hour = SEC // 3600
        minuate = (SEC % 3600) // 60
        sec = (SEC % 3600) % 60
        print('{}시간 {}분 {}초'.format(hour, minuate, sec))
    else:
        print('입력값이 올바르지 않습니다.')


#3 사분면 알아내기
# 입력받은 두 수가 ( - )인지 아닌지 판단하여 구현
def get_quadrant(POS_x, POS_y):
    if POS_x > 0 and POS_y > 0:
        print(1)
    elif POS_x < 0 and POS_y > 0:
        print(2)
    elif POS_x < 0 and POS_y < 0:
        print(3)
    elif POS_x > 0 and POS_y < 0:
        print(4)
    else:
        print('입력값이 올바르지 않습니다.')

#4 구구단
# 예제와 같이 표현하기 위하여 구현한 코드
# 1부터 3까지의 구구단을 우선적으로 출력하기 위해서
# for문과 while문 활용
# while문에서 k는 초기화가 반복되고, for문에서 j는 1부터 9까지 한줄씩 출력되기 때문에
# 예제와 같은 출력을 가지게 된다.
def multiplication():
    for j in range(1, 10):
        k = 0
        while k != 3:
            k += 1
            print('{} * {} = {}'.format(k, j, k*j), end = '\t')
        print('\n')
    print('\n')
    for j in range(1, 10):
        k = 3
        while k != 6:
            k += 1
            print('{} * {} = {}'.format(k, j, k*j), end = '\t')
        print('\n')
    print('\n')
    for j in range(1, 10):
        k = 6
        while k != 9:
            k += 1
            print('{} * {} = {}'.format(k, j, k*j), end = '\t')
        print('\n')

#5 응용 별 찍기
# 예제와 같이 입력받은 숫자 N개의 별을 출력하고, 다음 줄에는 space만큼 공백을 삽입하고, N-2개씩 별을 출력한다.
# 마지막 N-2의 값이 0이거나 1이면 증가한 space만큼 공백을 삽입하고 마지막 출력값인 별 하나를 출력한다.
def star(N):
    myValue = N
    space = 0
    for i in range(myValue):
        if myValue == 0 or myValue == 1: break
        print((' ' * space) + '*' * myValue)
        myValue -= 2
        space += 1
    print(' ' * space + '*')
        


#1
# get_credits(120)

#2
# time_converter2(7273)

#3
# get_quadrant(9, -13)

#4
# multiplication()

#5
# star(5)