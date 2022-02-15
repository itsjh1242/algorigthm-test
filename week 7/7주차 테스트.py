# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).

def solution():
    def isEmpty(): return len(myStack) == 0
    while True:
        myStack = []
        sentence = list(input('문장을 입력하세요 : '))
        if len(sentence) == 1 and sentence[0] == '.': return False
        for i in sentence:
            if i == '(':
                myStack.append(i)
            elif i == '[':
                myStack.append(i)
            elif i == ')' and not isEmpty():
                last_char = myStack[-1]
                if last_char == '(':
                    myStack.pop()
                else:
                    print('no')
                    myStack = [-1]
                    break
            elif i == ']' and not isEmpty():
                last_char = myStack[-1]
                if last_char == '[':
                    myStack.pop()
                else:
                    print('no')
                    myStack = [-1]
                    break
        print('yes') if isEmpty() else print('no')
                    
solution()
