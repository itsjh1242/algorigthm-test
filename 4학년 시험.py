import sys

def task_1():
    N = int(sys.stdin.readline())
    answer = 0
    while N >= 0:
        if N % 5 == 0:
            answer += (N // 5)
            return print(answer)
        N -= 3
        answer += 1
    else:
        print(-1)

def task_2():
    floor = int(input('층을 입력하세요 : '))
    num = int(input('호실을 입력하세요 : '))
    floorArr = [_ + 1 for _ in range(num)]
    for _ in range(floor):
        for __ in range(1, num):
            floorArr[__] += floorArr[__ - 1]
    print(floorArr[num - 1])
# task_1()
# task_2()
