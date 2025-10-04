from game import Game
game = Game()

while True:
    user_play = input('Welcome to slots! Type "play" to play! ')

    while True:
        if user_play == "play":
            print(f"You have {game.tokens} tokens!")

            try:
                user_bet = int(input("Enter a bet: "))
            except ValueError:
                continue

            if user_bet > game.tokens:
                print("You don't have enough tokens!")
                continue

            game.make_bet(user_bet)
            game.spin()
            print(game.result)
            game.check_win()

            if game.tokens <= 0:
                print("You are out of tokens!")
                quit()

            break

        elif user_play == "tokens":
            print(f"You have {game.tokens} tokens!")
            break

        elif user_play == "quit":
            quit()

        else:
            break