def task_1():
    N = int(input('정수 N을 입력하세요 : '))
    array = list(map(int, input('{}개의 숫자를 입력하세요'.format(N)).split()))
    print(min(array), max(array))

def task_2():
    def quiz(string):
        value, returnValue = 0, 0
        for i in string:
            if i == 'O':
                value += 1
                returnValue += value
            else:
                value = 0
        return returnValue
    N = int(input('테스트 케이스의 개수를 입력하세요 : '))
    for i in range(N):
        string = input('{}번 OX퀴즈의 결과를 입력하세요 : '.format(i + 1))
        print(quiz(string))

def task_3():
    C = int(input('테스트 케이스 개수를 입력하세요 : '))
    for i in range(C):
        N = list(map(int, input('{}번 테스트 케이스를 입력하세요 : '.format(i + 1)).split()))
        average = sum(N[1:]) / N[0]
        inc_Value = 0
        for j in N[1:]:
            if j > average: inc_Value += 1
        print('{:.3f}'.format(inc_Value / N[0] * 100))
    
def task_4():
    N = int(input('정수를 입력하세요 : '))
    _spc1, _spc2 = N - 1, 1
    print(' ' * _spc1 + "*")
    for i in range(1, N):
        _spc1 -= 1
        print(' ' * _spc1 + '*' + ' ' * _spc2 + '*')
        _spc2 += 2

def task_5():
    N = int(input('정수 N을 입력하세요 : '))
    pattern = ['*', '* *', '*****']
    left_space = N - 1
    for i in range(N):
        j = i % 3
        print(' ' * left_space + pattern[j] + '\n')
        left_space -= 1



# task_1()
# task_2()
# task_3()
# task_4()
# task_5()