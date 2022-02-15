def task_1():
    N = list(input('입력하세요 : '))
    myDict = {}
    for i in N:
        if i in myDict: myDict[i] += 1
        else: myDict[i] = 1
    myDict = {v : k for k, v in myDict.items()}
    print(myDict[max(myDict)])

def task_2():
    N = int(input('N을 입력하세요 : '))
    for i in range(N):
        answer = ''
        n, char = input('입력하세요 : ').split()
        for j in char: answer += (int(n) * j)
        print(answer)

def task_3():
    print(sum(list(map(int, input('N을 입력하세요 : ')))))

def task_4():
    dial = [
        ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'],
        ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']
        ]
    N = list(input('입력하세요 : '))
    answer = 0
    for i in N:
        for num, k in enumerate(dial):
            if i in k:
                answer += (num + 3)
    print(answer)

def task_5():
    print(len(list(input('문장을 입력하세요 : ').strip().split(' '))))



    



# task_1()
# task_2()
# task_3()
# task_4()
# task_5()
