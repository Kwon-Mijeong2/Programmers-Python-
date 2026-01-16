def solution(s):
    stack = []

    for i in s.split():
        if i == "Z":
            stack.pop()
        else:
            stack.append(i)

    return sum(list(map(int, stack)))