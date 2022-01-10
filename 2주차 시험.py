def task_1():
    N, X = map(int, input("N과 X를 입력하여 주세요 : ").split())
    A = list(map(int, input("수열 A를 입력하여 주세요 : ").split()))
    myl = [i  for i in A if i < X]
    print(myl)


def task_2():
    N = int(input("몇 명이 설문조사에 참여했습니까? : "))
    agree, disagree = 0, 0
    for i in range(N):
        if int(input("{}번 설문자의 의견은? : ".format(i + 1))) == 1:
            agree += 1 
        else:
            disagree += 1
    if agree == disagree: return print('Same result at Voting!')
    print('Junhee is cute!') if agree > disagree else print('Junhee is not cute!')
            

def task_3():
    N = int(input("정수를 입력하세요 : "))
    space = N - 1
    for i in range(N - 1):
        print(' ' * space + '*' * (i + 1))
        space -= 1
    print('*' * N)
    space = N - (N - 1)
    for i in range(N - 1, 0, -1):
        print(' ' * space + '*' * i)
        space += 1




# task_1()
# task_2()
# task_3()