def task_1():
    count = 1
    command = ['push', 'pop', 'size', 'empty', 'top', 'exit']
    stack = []
    def isEmpty():
        if not stack: return True
    while True:
        user_input = input('({})번째 명령어를 입력하세요 : '.format(count))
        if user_input[:4] == 'push':
            extra = user_input[5:]
            stack.append(extra)
        elif user_input == 'pop': print(stack.pop(-1)) if not isEmpty() else print(-1)
        elif user_input == 'size': print(len(stack))
        elif user_input == 'empty': print('1') if isEmpty() else print('0')
        elif user_input == 'top': print(stack[-1]) if not isEmpty() else -1
        else: break
        count += 1

def task_2():
    N = int(input('N을 입력하세요 : '))
    stack = []
    for i in range(N):
        user_input = list(input().split(', '))
        for command in user_input:
            if command == '0': stack.pop(-1)
            else: stack.append(command)
        print('Current Stack -> {}'.format(stack))
    print('Correct Sum -> {}'.format(sum(stack)))

def task_3():
    N = int(input('N을 입력하세요 : '))
    stack = []
    answer = []
    current_max_value = 0
    for i in range(N):
        command = int(input('숫자를 입력하세요 : '))
        if command > current_max_value:
            while command != current_max_value:
                current_max_value += 1
                stack.append(current_max_value)
                answer.append('+')
            stack.pop()
            answer.append('-')
        else:
            except_variable = stack.pop()
            answer.append('-')
            if command != except_variable:
                answer = ['no']
                break
    print('\n'.join(answer))
        

# task_1()
# task_2()
task_3()