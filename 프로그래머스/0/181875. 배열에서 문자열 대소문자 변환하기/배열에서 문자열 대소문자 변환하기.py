def solution(strArr):
    answer = []
    for i in range(0, len(strArr)):
        str = strArr[i]
        if i % 2 == 1:
            answer.append(str.upper())
        else:
            answer.append(str.lower())
    return answer