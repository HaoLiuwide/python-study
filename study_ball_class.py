import random


class player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0

    def winServe(self):
        return random.random() < self.prob

    def incScore(self):
        self.score += 1

    def getScore(self):
        return self.score


class RBallGame:
    def __init__(self, prob_a, prob_b):
        self.playA = player(prob_a)
        self.playB = player(prob_b)
        self.serve = self.playA

    def isOver(self):
        a, b = self.getScores()
        return a == 15 or b == 15 or (a == 7 and b == 0) or (a == 0 and b == 7)

    def serveChange(self):
        if self.serve == self.playA:
            self.serve = self.playB
        else:
            self.serve = self.playA

    def play(self):
        while not self.isOver():
            if self.serve.winServe():
                self.serve.incScore()
            else:
                self.serveChange()

    def getScores(self):
        return self.playA.getScore(), self.playB.getScore()


class simStats:
    def __init__(self):
        self.wins_a = 0
        self.wins_b = 0
        self.shuts_a = 0
        self.shuts_b = 0

    def update(self, aGame):
        a, b = aGame.getScores()
        if a > b:
            self.wins_a += 1
            if b == 0:
                self.shuts_a += 1

        else:
            self.wins_b += 1
            if a == 0:
                self.shuts_b += 1

    def printReport(self):
        n = self.wins_a + self.wins_b
        print('summary of'.capitalize(), n, 'games:\n')
        print('           wins(% total)         shutouts (% wins)')
        print('--------------------------------------------------')
        self.printLine('A', self.wins_a, self.shuts_a, n)
        self.printLine('B', self.wins_b, self.shuts_b, n)

    def printLine(self,label, wins, shuts, n):
        template = 'Player {0}: {1:5}  ({2:5.1%}) {3:11} ({4})'
        if wins == 0:
            shutStr = '----'
        else:
            shutStr = '{0:4.1%}'.format(float(shuts/wins))
        print(template.format(label, wins, float(wins)/n, shuts, shutStr))


def getInputs():
    pro_a = float(input('Please input a\'s prob: '))
    pro_b = float(input('Please input b\'s prob: '))
    n = int(input('Please input simulating times:  '))
    return pro_a, pro_b, n


def main():
    prob_a, prob_b, n = getInputs()
    status = simStats()
    for i in range(n):
        theGame = RBallGame(prob_a, prob_b)
        theGame.play()
        status.update(theGame)
    status.printReport()


if __name__ == '__main__':
    main()
