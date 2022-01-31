def task_1():
    n = int(input('논문의 총 인용 횟수를 입력하세요 : '))
    N = list(map(int, input('논문의 인용 횟수를 입력하세요 : ').split()))
    count = 0
    N.sort()
    
    for i in range(len(N)):
        if N[i] >= len(N) - i: #리스트의 길이에서 i만큼 빼주는 이유는; 정렬되어 있는 리스트에서 i번째 값 이후의 수들은 모두 i보다 크기때문
            print(len(N) - i)
            return 0
def task_2():
    N = int(input('N을 입력하세요 : '))
    def function(N):
        process, count = [N], 0
        while N != 1:
            if N % 3 == 0:
                N /= 3
            elif (N - 1) % 3 == 0:
                N -= 1
                process.append(int(N))
                count += 1
                N /= 3
            elif N % 2 == 0:
                N /= 2
            elif (N - 1) % 2 == 0:
                N -= 1
                process.append(int(N))
                count += 1
                N /= 2
            else:
                N -= 1
            count += 1
            process.append(int(N))
        return process, count
    process, count = function(N)
    print(count)
    for i in process: print(i, end = ' ')
task_1()
# task_2()

