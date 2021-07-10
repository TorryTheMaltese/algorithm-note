def solution(s):
    num_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }

    while not s.isdigit():
        for key in num_dict.keys():
            if s.find(key) >= 0:
                s = s.replace(key, num_dict[key])

    answer = int(s)

    return answer


if __name__ == "__main__":
    s = "one4seveneight"

    print(solution(s))
