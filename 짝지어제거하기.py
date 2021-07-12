def solution(s):
    stack = []
    top = ''
    for char in s:
        if top == char:
            stack.pop()
        else:
            stack.append(char)
        if len(stack) > 0:
            top = stack[-1]
        else:
            top = ''

    if len(stack) == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    s = "baabaa"
    print(solution(s))
