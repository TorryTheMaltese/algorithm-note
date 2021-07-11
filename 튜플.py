def solution(s):
    s = list(map(str, s[1:-1].split('},{')))

    for i in range(len(s)):
        if s[i].find('{') >= 0:
            s[i] = s[i].replace('{', '')
        if s[i].find('}') >= 0:
            s[i] = s[i].replace('}', '')

        s[i] = list(map(int, s[i].split(',')))

    s.sort(key=len)

    answer = s.pop(0)

    for set in s:
        answer += [el for el in set if el not in answer]

    return answer


if __name__ == '__main__':
    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

    print(solution(s))
