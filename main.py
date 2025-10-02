from game import Game

running = True
game = Game()

while running:
    user_play = input('Welcome to slots! Type "play" to play! ')
    if user_play == "play":
        print(f"You have {game.tokens} tokens!")
        user_bet = int(input("Enter a bet: "))
        game.make_bet(user_bet)
        game.spin()
        print(game.result)
        game.check_win()


    else:
        continue


