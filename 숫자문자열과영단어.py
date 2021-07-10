def solution(s):
    while not s.isdigit():
        if s.find("one") >= 0:
            s = s.replace("one", '1')
        elif s.find("two") >= 0:
            s = s.replace("two", "2")
        elif s.find("three") >= 0:
            s = s.replace("three", "3")
        elif s.find("four") >= 0:
            s = s.replace("four", "4")
        elif s.find("five") >= 0:
            s = s.replace("five", "5")
        elif s.find("six") >= 0:
            s = s.replace("six", "6")
        elif s.find("seven") >= 0:
            s = s.replace("seven", "7")
        elif s.find("eight") >= 0:
            s = s.replace("eight", "8")
        elif s.find("nine") >= 0:
            s = s.replace("nine", "9")
        elif s.find("zero") >= 0:
            s = s.replace("zero", "0")

    answer = int(s)

    return answer


if __name__ == "__main__":
    s = "one4seveneight"

    print(solution(s))
