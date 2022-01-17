def task_1():
    N = int(input('N을 입력하세요 : '))
    num = sum(list(map(int,input('숫자 {}개를 입력하세요 : '.format(N)))))
    print(num)

def task_2():
    preN = False
    while True:
        N = float(input('혼합물의 온도를 입력하세요 : '))
        if N == 999: break
        if not preN:
            preN = N
        else:
            print('{:.2f}'.format(N - preN))
        preN = N

def task_3():
    while True:
        N = list(map(int, input().split()))
        if sum(N) == 0: break
        # Invalid
        def Invalid_(arr):
            arr.sort(reverse = True)
            if arr[2] <= arr[0] + arr[1]:
                return True
        # Equilateral
        def Equilateral_(arr):
            if arr[0] == arr[1] == arr[2]: return True
        # Scalene
        def Scalene_(arr):
            if arr[0] != arr[1] == arr[2]: return True
        def Isosceles_(arr):
            arr.sort(reverse = True)
            if arr[0] == arr[1] and arr[0] != arr[2] and arr[1] != arr[2]: return True
        if Equilateral_(N): return(print('Equilateral'))
        if Invalid_(N): return(print('Invalid'))
        if Isosceles_(N): return(print('Isosceles'))
        if Scalene_(N): return(print('Scalene'))


            




# task_1()
# task_2()
# task_3()