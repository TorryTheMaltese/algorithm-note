def solution(s):
    str_len = len(s)
    max_len = str_len // 2
    if max_len == 0:
        max_len = 1
    cnt = 9999

    for cut_by in range(1, max_len + 1):
        i = 0
        note = []
        old = ''
        while i < str_len:
            tmp = s[i:i + cut_by]
            if tmp == old:
                note[-1][0] += 1
            else:
                note.append([1, tmp])
            old = tmp
            i += cut_by

        res = ""
        for substring in note:
            if substring[0] > 1:
                res = res + str(substring[0]) + substring[1]
            else:
                res = res + substring[1]

        if len(res) < cnt:
            cnt = len(res)

    return cnt


if __name__ == '__main__':
    s = "aabbaccc"

    print(solution(s))
