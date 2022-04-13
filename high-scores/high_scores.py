def latest(scores):
    return scores[-1]
    #pass


def personal_best(scores):
    best_scores = sorted(scores)
    return best_scores[-1]
    #pass


def personal_top_three(scores):
    """
    if len(scores) < 3:
        return sorted(scores[:],reverse=True)
    else:
    """
    score_sort = sorted(scores,reverse=True)
    return score_sort[:3]
    #pass
