def task_1():
    N = int(input('수의 개수를 입력하세요 : '))
    myArr = []
    for i in range(N): myArr.append(int(input('{}번째 수를 입력하세요 : '.format(i + 1))))
    # 산술평균
    print('{:.0f}'.format(sum(myArr) // N))
    # 중앙 값 ( N이 홀수라고 가정했으니, 짝수일 경우의 중앙 값은 생략 )
    middle_arr = sorted(myArr)
    print(middle_arr[len(middle_arr) // 2])
    # 최빈값
    countDict = {}
    for i in myArr: countDict[i] = myArr.count(i)
    print(max(countDict.values()) or middle_arr[1])
    # 범위
    print(middle_arr[-1] - middle_arr[0])
    
    
def task_2(array, commands):
    answer = []
    for i in commands:
        new_num = sorted(array[i[0] - 1:i[1]])
        answer.append(new_num[i[2] - 1])
    print(answer)

def task_3(array):
    N = sorted(map(str, array), key = lambda x : x * 3, reverse = True)
    # x * 3 => 정수 범위 : 1000
    # 1의 자리 수를 3번 string으로 더했을 때, 1000 이하 값이 나옴
    print(str(int(''.join(N))))
    # answer = []
    # for i in array:
    #     flag = False
    #     myStr = "" + str(i)
    #     for j in range(len(array)):
    #         if i == array[j] and not flag:
    #             flag = True
    #         else:
    #             myStr += str(array[j])
    #     answer.append(myStr)
    # print(answer)


        
# task_1()
# task_2([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
# task_3([6, 10, 2])
# task_3([3, 30, 34, 5, 9])
