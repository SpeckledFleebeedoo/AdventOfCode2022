with open("day2/input.txt") as f:
    lines = f.readlines()

choicescores = {"A": {"X": 3, "Y": 1, "Z": 2},
                "B": {"X": 1, "Y": 2, "Z": 3},
                "C": {"X": 2, "Y": 3, "Z": 1}}

roundscores = {"Z": 6, "Y": 3, "X": 0}

score = 0
for round in lines:
    round = round.strip()
    opponent, me = round.split(" ")
    roundscore = roundscores[me]
    choicescore = choicescores[opponent][me]
    score += roundscore + choicescore

print(score)
