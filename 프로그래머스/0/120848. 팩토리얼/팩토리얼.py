def solution(n):
    answer = 0
    result = 1
    while n >= result:
        answer += 1
        result *= answer
    return answer -1