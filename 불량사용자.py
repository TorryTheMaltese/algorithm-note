import re
from itertools import product


def solution(user_id, banned_id):
    result = []

    for bad in banned_id:
        tmp = []
        for id in user_id:
            if re.match(bad.replace('*', '.') + '$', id):
                tmp.append(id)
        result.append(tmp)

    answer = []
    for i in list(product(*result)):
        tmp = frozenset(i)
        if len(tmp) == len(banned_id):
            answer.append(tmp)

    return len(set(answer))


if __name__ == '__main__':
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]

    print(solution(user_id, banned_id))
