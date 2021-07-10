def solution(record):
    users = {}
    answer = []
    result = []
    for r in record:
        info = r.split()
        if info[0] == 'Enter':
            users[info[1]] = info[2]
            answer.append([info[1], "님이 들어왔습니다."])
        elif info[0] == "Leave":
            answer.append([info[1], "님이 나갔습니다."])
        else:
            users[info[1]] = info[2]

    for ans in answer:
        result.append(users[ans[0]] + ans[1])

    return result


if __name__=="__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

    print(solution(record))
