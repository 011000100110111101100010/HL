# checks user enters yes/y or no/n and returns that
def yes_no(question):
    error = "Please enter yes or no"

    while True:

        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(error)


def instructions_text():
    print('''At the start of each round, the user and the computer each roll a die.
    The initial number of points for each player is the total shown by the die.Then, taking turns,
    the user and computer each roll a single die and add the result to their points.
    The goal is to get 13 points (or slightly less) for a given round.
    Once you are happy with your number of points, you can ‘pass’.
    -If you go over 13, then you lose the round (and get zero points). If the computer goes over 13,
    the round ends and your score is the number of points that you have earned.
    -If the computer gets more points than you (eg: you get 10 and they get 11, then you lose your score stays
    the same).
    -If you get more points than the computer (but less than 14 points), you win and add your points to your
    score. The computer’s score stays the same.
    -The ultimate winner of the game is the first one to get to the specified score goal.
    .''')

# checks any ingegers and
def int_checker(question):
    error = "please enter an integer above 1"
    while True:
        value = input(question)
        if value == "":
            return ""

        try:
            intvalue = int(value)

            if intvalue > 1:
                return intvalue

            else:
                print(error)

        except ValueError:
            print(error)

# *** main routine ***
rounds_played = 0
mode = 0
print()
print("🔼🔼🔼 Welcome to the Higher Lower Game 🔽🔽🔽")

want_instructions = yes_no("do you want to read the instrustions? ")

print(want_instructions)

round_num = int_checker("how many rounds would you like to play to press enter for infinite")
if round_num == "":
    mode = "Infinite"
    round_num = 20
else:
    mode = "Normal"

while round_num > rounds_played:
    rounds_played += 1
    round_heading = f"\nRound {rounds_played} ({mode} mode)"
    print(round_heading)


    if mode == "Infinite":
        round_num += 10