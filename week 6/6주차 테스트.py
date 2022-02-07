def task_1():
    print(''.join(sorted(input('N을 입력하세요 : '))))

def task_2():
    N = int(input('N을 입력하세요 : '))
    myl , myArr= list(map(int, input('좌표를 입력하세요 : ').split())), [0 for _ in range(N)]
    for i in myl:
        for j in range(len(myl)):
            if i < myl[j]:
                myArr[j] += 1
    print(myArr)


# task_1()
# task_2()