def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    min_count = 0
    max_count = 0
    for score in scores:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1
    return [max_count, min_count]