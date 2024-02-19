import random

options = ("heads", "tails")

game_play = True

while game_play:

    player = None
    coin = random.choice(options)

    while player not in options:
        player = input("Heads or tails?")

    print(f"Coin:{coin}")

    if player == coin:
        print("You win!")
    else:
        print("You lose")

    if not input("Play again? (y/n)").lower() =="y":
        game_play = False

print("Thank you for playing! :)")


