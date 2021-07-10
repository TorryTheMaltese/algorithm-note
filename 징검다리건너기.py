def solution(stones, k):
    cnt = 0
    kinds_of_stones = sorted(list(set(stones)))
    lens_of_stones = len(stones)

    min_niniz = 0
    max_niniz = len(kinds_of_stones) - 1

    while min_niniz < max_niniz:
        avg_index = (min_niniz + max_niniz) // 2
        niniz_passed = kinds_of_stones[avg_index]
        tmp = [stone - niniz_passed for stone in stones]

        broken_part_cnt = 0
        broken = 0
        for i in range(lens_of_stones):
            if tmp[i] < 0:
                broken += 1
                if broken_part_cnt < broken:
                    broken_part_cnt = broken
            else:
                broken = 0

        if broken_part_cnt < k:
            cnt = niniz_passed
            min_niniz = avg_index + 1
        elif broken_part_cnt >= k:
            max_niniz = avg_index

    return cnt


if __name__ == '__main__':
    stones_input = [2]
    k_input = 1

    print(solution(stones_input, k_input))
