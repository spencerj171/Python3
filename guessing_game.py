from random import randint
is_game_over = False
tries = 3
play_again = ""

while not is_game_over:
    print("*****The Guessing Game*****")
    rand = randint(1, 10)
    count = 0

    while count <= tries:
        guess = int(input("What number am I thinking of? "))
        if guess == rand:
            print("You guessed it\n")
            break
        elif guess != rand and count == tries:
            print("Sorry, you lose\n")
            break
        elif guess < rand:
            print("Too low\n")
            count += 1
        else:
            print("Too high\n")
            count += 1

    while play_again != "y" or play_again != "n":
        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again == "y":
            break
        elif play_again =="n":
            is_game_over = True
            break
        else:
            print("Please enter 'y' for 'yes' or 'n' for 'no'")

print("Thanks for playing")
