def task_1():
    N = int(input('수열의 크기를 입력하세요 : '))
    array = list(input('수열을 입력하세요 : ').split())
    answer = []
    for _ in range(len(array) - 1):
        max_num = 0
        for i in range(_ + 1, len(array)):
            if array[i] > array[_]:
                max_num = array[i]
                break
            else:
                max_num = -1

        answer.append(max_num)
    answer.append(-1)
    print(answer)
task_1()
        