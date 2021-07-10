def solution(p):
    length_p = len(p)
    answer = ''

    if length_p == 0:
        return answer

    u, v = separate_string(p)
    return check_what_is_correct(u, v)


def separate_string(w):
    u, v = w, ''
    length_w = len(w)
    check_balance = 0

    if length_w == 0:
        return '', ''

    for i in range(length_w):
        if w[i] == '(':
            check_balance += 1
        elif w[i] == ')':
            check_balance -= 1

        if check_balance == 0:
            u = w[:i + 1]
            v = w[i + 1:]
            break
    return u, v


def is_correct(string):
    stack_tmp = []
    if len(string) > 0:
        for s in string:
            if s == '(':
                stack_tmp.append(s)
            elif s == ')':
                if len(stack_tmp) > 0:
                    stack_tmp.pop()
                else:
                    return False
    if len(stack_tmp) == 0:
        return True
    else:
        return False


def check_what_is_correct(u, v):
    first = is_correct(u)
    second = is_correct(v)
    answer = ''

    if first and second:
        answer = u + v
    elif first:
        u_tmp, v_tmp = separate_string(v)
        answer = u + check_what_is_correct(u_tmp, v_tmp)
    elif not first:
        u_tmp, v_tmp = separate_string(v)
        answer = '(' + check_what_is_correct(u_tmp, v_tmp) + ')' + reverse_string(u[1:-1])
    return answer


def reverse_string(string):
    reversed_string = ''

    reverse_dict = {
        '(': ')',
        ')': '('
    }

    for s in string:
        reversed_string += reverse_dict[s]

    return reversed_string


if __name__ == '__main__':
    input_string = ")("

    print(solution(input_string))
