from random import randint

choices = ["rock", "paper", "scissors"]
is_game_over = False

print('Rock...')
print('Paper...')
print('Scissors...\n')

print("To exit, type 'quit'\n")

while not is_game_over:
    p1 = input('Make your move: ').lower()
    if p1 == "quit":
        print("Thanks for playing\n")
        is_game_over = True
    else:
        comp = choices[randint(0, 2)]
        print("Computer chose " + comp)
        if p1 == comp:
            print("It's a draw\n")
        elif p1 == "rock":
            if comp == "paper":
                print("Computer wins\n")
            elif comp == "scissors":
                print("You win\n")
        elif p1 == "paper":
            if comp == "rock":
                print("You win\n")
            elif comp == "scissors":
                print("Computer wins\n")
        elif p1 == "scissors":
            if comp == "rock":
                print("Computer wins\n")
            elif comp == "paper":
                print("You win\n")
        else:
            print("Please enter a valid move\n")
