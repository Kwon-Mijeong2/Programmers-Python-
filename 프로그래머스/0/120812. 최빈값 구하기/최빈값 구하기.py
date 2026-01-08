def solution(array):
    value = []
    count = []

    for i in range(len(array)):
        if array[i] not in value:
            value.append(array[i])

    for i in range(len(value)):
        count.append(array.count(value[i]))

    if count.count(max(count)) != 1:
        answer = -1
    else: answer = value[count.index(max(count))]
    
    return answer