def solution(n):
    answer = []

    def hanoi(n, s, e, t, moves):
        if n == 1:
            moves.append([s, e])
            return
        hanoi(n-1, s, t, e, moves)
        moves.append([s, e])
        hanoi(n-1, t, e, s, moves)

    hanoi(n, 1, 3, 2, answer)
    return answer
