# 1번 문제 
# 윤년 
# 윤년이란, 연도가 4의 배수이면서 100의 배수가 아닐 때 또는 400의 배수일 때를 말합니다.
def solution1(year):
    print('1') if (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0) else print('0')


# 2번 문제
# 별 N번 출력

def solution2(N):
    for i in range(N):
        for j in range(N, i + 1, -1):
            print(' ', end = '')
        print('*' * (i + 1))


# 3번 문제
# 아스키 코드 값 출력

def solution3(C):
    print(ord(C))


solution1(2012)
print('\n')
solution2(5)
print('\n')
solution3('B')
