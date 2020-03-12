def latest(scores):
    return scores[-1]


def personal_best(scores):
    best = scores[0]
    for i in range(len(scores)):
        for x in scores:
            if best < scores[i]:
                best = scores[i]
    return best


def personal_top_three(scores):
    top_three = []
    if len(scores) == 3 or len(scores) > 3:
        for i in range(3):
            top_three.append(max(scores))
            scores.remove(max(scores))
        return top_three
    else:
        for i in range(len(scores)):
            top_three.append(max(scores))
            scores.remove(max(scores))
        return top_three
