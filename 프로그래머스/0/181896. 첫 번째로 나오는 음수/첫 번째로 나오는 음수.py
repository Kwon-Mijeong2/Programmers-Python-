def solution(num_list):
    answer = 0
    cnt = -1
    for i in num_list:
        cnt += 1
        if i < 0:
            answer = cnt
            break
        else:
            answer = -1
    return answer