def solution(before, after):
    answer = 0
    b = list(before)
    a = list(after)
    b.sort()
    a.sort()
    if a == b:
        answer = 1
    return answer