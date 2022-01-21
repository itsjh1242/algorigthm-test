# Last Edit
# 2022.01.17 _ 16:47
# 2022.01.17 _ 17:20
# 2022.01.21 _ 20:06

def task_1():
    N = int(input('N을 입력하세요 : '))
    num = sum(list(map(int,input('숫자 {}개를 입력하세요 : '.format(N)))))
    print(num)

def task_2():
    preN = False # previous Nunber
    while True: # Infinity while loop
        N = float(input('혼합물의 온도를 입력하세요 : ')) 
        if N == 999: break # condition of break
        if not preN: # if preN == False
            preN = N # 첫 번째 값을 저장하기 위한 목적
        else:
            print('{:.2f}'.format(N - preN))
            preN = N # 이전 값을 저장하기 위한 목적

def task_3():
    while True:
        N = list(map(int, input('세 변의 길이를 입력하세요 : ').split()))
        if sum(N) == 0: break
        # Invalid
        def Invalid_(arr):
            arr.sort()
            if arr[2] >= sum(arr[0:2]):
                return True
        # Equilateral
        def Equilateral_(arr):
            if arr[0] == arr[1] == arr[2]: return True
        # Scalene
        def Scalene_(arr):
            if arr[0] != arr[1] != arr[2]: return True
        # Isosceles
        def Isosceles_(arr):
            arr.sort()
            if (arr[1] + arr[2]) / 2 == arr[1]: return True
        
        if Invalid_(N): print('Invalid')
        elif Equilateral_(N): print('Equilateral')
        elif Isosceles_(N): print('Isosceles')
        elif Scalene_(N): print('Scalene')
        
    print('*' * 10 + '\n0 0 0을 입력해서 프로그램이 종료 되었습니다.\n' + '*' * 10)


            

# task_1()
# task_2()
# task_3()
