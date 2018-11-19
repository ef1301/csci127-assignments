def score(w):
    upper = w.upper()
    score_count = 0
    one = "AEIOULNRST"
    two = "DG"
    three = "BCMP"
    four = "FHVWY"
    five = "K"
    eight = "JX"
    ten = "QZ"
    for item in upper:
        if item in one:
            score_count += 1
        elif item in two:
            score_count += 2
        elif item in three:
            score_count += 3
        elif item in four:
            score_count += 4
        elif item in five:
            score_count += 5
        elif item in eight:
            score_count += 8
        elif item in ten:
            score_count += 10
    return score_count

print(score("AEIOU"))
print(score("hello"))
print(score("Emily"))
