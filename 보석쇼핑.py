def solution(input):
    gem_name = set(input)
    gem_nums = len(gem_name)
    input_size = len(input)

    lt = 0
    note = {}
    answer = [0, input_size-1]

    for rt in range(0, input_size):
        if note.get(input[rt]):
            note[input[rt]] += 1
        else:
            note[input[rt]] = 1

        while len(note) == gem_nums:
            if answer[1] - answer[0] > rt - lt:
                answer = [lt, rt]
            note[input[lt]] -= 1
            if note[input[lt]] == 0:
                del note[input[lt]]
            lt += 1

    answer = [answer[0] + 1, answer[1] + 1]
    return answer


if __name__ == '__main__':
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

    print(solution(gems))
