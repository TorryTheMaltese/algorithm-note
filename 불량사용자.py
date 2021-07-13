import re
from itertools import product
import copy

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # 라이브러리를 이용한 불량 사용자 풀이 # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# def solution(user_id, banned_id):
#     result = []
#
#     for bad in banned_id:
#         tmp = []
#         for id in user_id:
#             if re.match(bad.replace('*', '.') + '$', id):
#                 tmp.append(id)
#         result.append(tmp)
#
#     answer = []
#     for i in list(product(*result)):
#         tmp = frozenset(i)
#         if len(tmp) == len(banned_id):
#             answer.append(tmp)
#
#     return len(set(answer))


def solution(user_id, banned_id):
    result = []

    for bad in banned_id:
        tmp = []
        for id in user_id:
            if re.match(bad.replace('*', '.') + '$', id):
                tmp.append(id)
        result.append(tmp)

    tmp = dfs(result, 0, [], [])

    answer = []
    for t in tmp:
        if t not in answer:
            answer.append(t)

    return len(answer)


def dfs(arr, i, result, answer):
    arr_len = len(arr)
    if i == arr_len:
        s_result = set(result)
        if len(s_result) == arr_len:
            answer.append(copy.deepcopy(s_result))
    if i < arr_len:
        for a in arr[i]:
            result.append(a)
            dfs(arr, i + 1, result, answer)
            result.pop()
    return answer


if __name__ == '__main__':
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]

    print(solution(user_id, banned_id))
