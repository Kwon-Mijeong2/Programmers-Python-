def solution(num_list):
    answer = []
    cnt = 0
    num_list.sort()
    for i in num_list:
        answer.append(i)
        cnt += 1
        if cnt == 5:
            break
    return answer