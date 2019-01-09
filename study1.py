from random import random


def getInputs():
    pro_a = float(input('Please input a\'s prob: '))
    pro_b = float(input('Please input b\'s prob: '))
    n = int(input('Please input simulating times:  '))
    return pro_a, pro_b, n


def gameScore(pro_a, pro_b):
    a_score = 0
    b_score = 0
    shooter = 1
    game_count = 0
    while a_score != 15 and b_score != 15:
        if shooter == 1:
            if random() < pro_a:
                a_score += 1
            else:
                shooter = 2
        if shooter == 2:
            if random() < pro_b:
                b_score += 1
            else:
                shooter = 1
        game_count += 1
    return a_score, b_score


def simNGame(n, pro_a, pro_b):
    wins_a = 0
    wins_b = 0
    for i in range(n):
        a_score, b_score = gameScore(pro_a, pro_b)
        if a_score > b_score:
            wins_a += 1
        else:
            wins_b += 1
    return wins_a, wins_b


def printSummary(n,wins_a, wins_b):
    print('Game simulated:', n)
    print('Wins for A:{0:>4}({1:0.1%})'.format(wins_a, wins_a / n))
    print('Wins for B:{0:>4}({1:0.1%})'.format(wins_b, wins_b / n))


def main():
    pro_a, pro_b, n = getInputs()
    wins_a, wins_b = simNGame(n, pro_a, pro_b)
    printSummary(n, wins_a, wins_b)


if __name__ == "__main__":
    main()
