def solution(emergency):
    answer = []
    sor = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(sor.index(i)+1)
    return answer