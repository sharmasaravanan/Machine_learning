class RPS:
    def __init__(self):
        self.p1 = input("Enter your name: ")
        self.p2 = input('Enter your name: ')
        self.temp = {self.p1: 0, self.p2: 0}
        self.options = ['rock', 'paper', 'scissor']

    def check(self):
        if self.user1 in self.options and self.user2 in self.options:
            if self.user1 == self.user2:
                return "Game is tie"
            elif self.user1 == "rock":
                if self.user2 == "scissor":
                    self.temp[self.p1] += 1
                else:
                    self.temp[self.p2] += 1
            elif self.user1 == "scissor":
                if self.user2 == "paper":
                    self.temp[self.p1] += 1
                else:
                    self.temp[self.p2] += 1
            elif self.user1 == "paper":
                if self.user2 == "rock":
                    self.temp[self.p1] += 1
                else:
                    self.temp[self.p2] += 1
        else:
            return "Invalid options"

    def winner(self):
        winnerDict = dict(sorted(self.temp.items(), key=lambda kv: kv[1]))
        return f'{winnerDict.popitem()[0]} is the winner of the game'

    def play(self):
        self.user1 = input("Enter your choice :")
        self.user2 = input("Enter your choice :")
        if self.user1 != 'q' or self.user2 != 'q':
            self.check()
        else:
            print("Good bye")
            return

rps = RPS()

for i in range(3):
    rps.play()

rps.winner()
