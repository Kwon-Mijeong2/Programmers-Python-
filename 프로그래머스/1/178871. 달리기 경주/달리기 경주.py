def solution(players, callings):
    answers = dict({player: i for i, player in enumerate(players)})
    for calls in callings:
        a = answers[calls]
        answers[calls] -= 1
        answers[players[a-1]] += 1
        players[a-1], players[a] = players[a], players[a-1]
    return players