def task_1():
    N = ''.join(sorted(map(str, input('N을 입력하세요 : ')), reverse = True))
    print(N)

def task_2():
    N = int(input('입력할 수의 개수를 입력하세요 : '))
    myArr = []
    for i in range(N): myArr.append(int(input('{}번 째 숫자를 입력하세요 : '.format(i + 1))))
    myArr.sort()
    for i in myArr: print(i)

def task_3():
    N = int(input('회원의 수를 입력하세요 : '))
    myArr = []
    for i in range(N):
        age, name = input('{}번 째 회원의 나이와 이름을 입력하세요 : '.format(i + 1)).split()
        myArr.append([int(age), name])
    myArr.sort(key = lambda x : x[0])
    for age, name in myArr: print(age, name)

def task_4():
    N = int(input('단어의 개수를 입력하세요 : '))
    wordArr, answer = [], []
    for i in range(N): wordArr.append(input('{}번째 단어를 입력하세요 : '.format(i + 1)))
    # condition 1 - 사전 순으로 정렬
    wordArr = sorted(wordArr)
    # condition 2 - 길이 순으로 정렬
    wordArr.sort(key = lambda x : len(x))
    # condition 3 - 중복 값 제거
    for i in wordArr:
        if not i in answer:
            answer.append(i)
            print(i)

def task_5():
    N = int(input('평면 위의 점 개수를 입력하세요 : '))
    dotArr = []
    for i in range(N): dotArr.append(input('{}번째 좌표 값을 입력하세요 : ').split())
    answer = sorted(dotArr, key = lambda x : x[0] + x[1])
    for x, y in answer:
        print(x, y)

# task_1()
# task_2()
# task_3()
# task_4()
# task_5()