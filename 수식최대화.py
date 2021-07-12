def solution(expression):
    operators = [['*', '-', '+'], ['*', '+', '-'], ['-', '*', '+'], ['-', '+', '*'], ['+', '-', '*'], ['+', '*', '-']]
    exp = []
    max_total = 0

    tmp = ''
    for s in expression:
        if s.isdigit():
            tmp += s
        else:
            exp.append(tmp)
            tmp = ''
            exp.append(s)
    exp.append(tmp)

    for ope in operators:
        arr_tmp = exp.copy()
        for o in ope:
            i = 0
            while i < len(exp) and i < len(arr_tmp):
                if arr_tmp[i] == o:
                    right = int(arr_tmp.pop(i + 1))
                    calc = arr_tmp.pop(i)
                    left = int(arr_tmp.pop(i - 1))

                    if calc == '*':
                        arr_tmp.insert(i - 1, left * right)
                    elif calc == '-':
                        arr_tmp.insert(i - 1, left - right)
                    elif calc == '+':
                        arr_tmp.insert(i - 1, left + right)
                    i = -1
                i += 1
        if max_total < abs(int(arr_tmp[0])):
            max_total = abs(int(arr_tmp[0]))
    return max_total


if __name__ == '__main__':
    s = "100-200*300-500+20"

    print(solution(s))
