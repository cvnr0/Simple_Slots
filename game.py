import random

class Game:
    def __init__(self, tokens=100):
        self.tokens = tokens

    def make_bet(self, bet_tokens):
        self.bet_tokens = bet_tokens
        self.tokens -= bet_tokens

    def spin(self):
        self.result = [random.randint(0,9), random.randint(0,9), random.randint(0,9)]

    def check_win(self):
        if self.result[0] == self.result[1] == self.result[2]:
            print("JACKPOT!!")
            print(f"YOU WIN {self.bet_tokens*2} TOKENS!!")
            self.tokens += self.bet_tokens*2

        elif self.result[0] == self.result[1] or self.result[1] == self.result[2] or self.result[0] == self.result[2]:
            print(f"You win {self.bet_tokens*1.5} tokens!")
            self.tokens += self.bet_tokens*1.5
        else:
            print("You lose! Better luck next time!")
