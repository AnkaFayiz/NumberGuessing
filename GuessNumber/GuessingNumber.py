import random

class Play:
    def GuessNumber(self):
        self.Guess = random.randint(1,100)
        self.PlayerGuest()

        if(self.PlayerGuest == self.Guess):
            print("You Won", self.Guess)
        else:
            print("You Lose" , self.Guess)


    def PlayerGuest(self):
        self.Guessing = int(input("Guess between 1 - 100 : "))


if __name__ == "__main__":
    app = Play()
    print(app.GuessNumber())
