def calculate_score(attendance, marks, quiz, assignment, previous_result):
    score = (
        attendance * 0.25
        + marks * 0.30
        + quiz * 0.15
        + assignment * 0.15
        + previous_result * 0.15
    )
    return score