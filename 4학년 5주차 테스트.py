import sys

def task_1():
    S = sys.stdin.readline()
    alphabet_table = [chr(i) for i in range(97, 123)]
    answer = []
    for _ in alphabet_table: answer.append(S.index(_)) if _ in S else answer.append(-1)
    print(answer)


def task_2():
    N = input('입력하세요 : ')
    table = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for _ in table:
        N = N.replace(_, '@')
    print(len(N))


# task_1()
task_2()
