def exam_score_averager(*scores):
    total = 0

    for score in scores:
        total += score

    average = total / len(scores)

    print("Average Score:", average)

exam_score_averager(80, 75, 90, 85)