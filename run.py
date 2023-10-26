import random
import os
from classes.colors import color


def clear_screen():
    """
    Defines function to clear the screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


DRAGON_LIST = ["knucker", "lung", "wyvern", "amphithere",
               "lindworm", "phoenix", "marsupial", "kirimu",
               "leviathan", "bakunawa", "imoogi", "kihawahine",
               "basilisk", "frost", "cockatrice", "serpent",
               "taniwha", "uwabami", "orochi", "zahhak"
               ]


def main_logo():
    """
    Print the name of the game
    """
    logo = [
        " ____",
        "|  _ \ _ __ __ _  __ _  ___  _ __  ___",
        "| | | | '__/ _` |/ _` |/ _ \| '_ \/ __|",
        "| |_| | | | (_| | (_| | (_) | | | \_ \_",
        "|____/|_|  \__,_|\__, |\___/|_| |_|___/",
        "                 |___/",
    ]
    for line in logo:
        print(color["orange"].apply_color(line))


def intro():
    """
    Introduces to game
    """
    game_intro = [
        "",
        "Welcome to the mystical world of Dragons!",
        "",
        "A captivating adventure that will test your knowledge of dragons.",
        "",
        "Each dragon has concealed its identity behind a web of letters,",
        "",
        "daring you to uncover its name, one letter at a time.",
        "",
        "The adventure awaits, and the dragon awaits your daring guesses.",
        ""
    ]
    for line in game_intro:
        print(color["yellow"].apply_color(line))


def game_rules(username):
    """
    Shows rules of the game if "yes" is chosen or
    if "no" is entered skips to verifying if player wants to play
    """
    rules = input(
        color["green"].apply_color("Would you like to see the rules (yes/no)?:\n")
        ).lower()

    if rules in ["yes", "y",]:
        clear_screen()
        # Display rules
        print("")
        print(color["green"].apply_color
              ("'Dragons' game rules")
              )
        print("")
        print(color["yellow"].apply_color
              ("1.Enter username to play")
              )
        print("")
        print(color["yellow"].apply_color
              ("2.Your mission is to guess the name of a concealed dragon")
              )
        print("")
        print(color["yellow"].apply_color
              ("3.You will be given a random dragon name to guess")
              )
        print("")
        print(color["yellow"].apply_color
              ("4.Guess one letter at a time")
              )
        print("")
        print(color["yellow"].apply_color
              ("5.You have 8 chances to guess")
              )
        print("")
        print(color["yellow"].apply_color
              ("6.Correct guess will reveal the letter")
              )
        print("")
        print(color["yellow"].apply_color
              ("7.Incorrect guess will add to attempt count")
              )
        print("")
        print(color["yellow"].apply_color
              ("8.When you guess the dragon or run out of attempts,")
              )
        print("")
        print(color["yellow"].apply_color
              ("dragon name and description will be revealed")
              )
        print("")

    elif rules in ["no", "n"]:
        # Skip to verifying if user wants to play
        continue_to_game(username)

    else:
        print(color["green"].apply_color("Please enter 'yes' or 'no'!"))


def continue_to_game(username):
    """
    Verifies user wants to play the game by entering y for yes or n for no
    """
    while True:
        choice = input(color["green"].apply_color
                       ("Would you like to play (yes/no)?:\n")
                       ).strip().lower()

        if choice in ["yes", "y"]:
            clear_screen()
            start_game(username, DRAGON_LIST)
            break
        if choice in ["no", "n"]:
            clear_screen()
            exit_game()
        else:
            print(color["green"].apply_color("Please enter 'yes' or 'no'"))


def exit_game():
    """
    Thanks user for visiting and exits game gracefully by returning to logo.
    """
    print(color["green"].apply_color("Thank you for visiting 'Dragons' game."))
    print("")
    print(color["green"].apply_color("Goodbye!"))
    main_logo()
    intro()


def enter_username():
    """
    Asks user to create a username consisting of 4 - 15 letters.
    """
    while True:
        print()
        username = input(color["green"].apply_color
                         ("Please enter username:\n")
                         )

        if " " in username:
            print(color["green"].apply_color
                  ("Username can't contain empty spaces!")
                  )

        elif len(username) < 4:
            print(color["green"].apply_color
                  ("Sorry, username has to contain at least 4 characters!")
                  )

        elif len(username) > 15:
            print(color["green"].apply_color
                  ("Sorry, username can't be longer than 15 characters!")
                  )

        elif not username.isalpha():
            print(color["green"].apply_color
                  ("Sorry, username can't have numbers or special characters!")
                  )

        else:
            return username


def random_name(dragon):
    """
    Function to choose random dragon name from the list.
    """
    dragon = DRAGON_LIST
    return random.choice(dragon)


def display_name(name, guessed_letters):
    """
    Shows the name with guessed letters
    """
    display = ""
    for letter in name:
        if letter in guessed_letters:
            display += letter
        else:
            display = ""
    return display


def start_game(username, dragon):
    """
    Loop for the game
    """
    dragon = DRAGON_LIST
    name_to_guess = random_name(dragon)
    guessed_letters = []
    attempts = 8  # Max number of attempts

    print(color["green"].apply_color(f"Welcome, {username}!"))
    print("")
    print(color["green"].apply_color
          (f"You have {attempts} attempts to guess the name.")
          )
    print("")

    # Create a dictionary for dragon descriptions and match them to name
    dragon_descriptions = {
        "knucker": "A type of water dragon from English folklore. \
                    Found in damp, wealden locations, near food sources such as rabbit warrens. \
                    Serpentine in appearance this dragon has only vestigial wings and cannot fly.",
        "lung": "A lung is most often found near rivers, streams and lakes \
                    that hide it's underwater nest. There are different types of lung dragons. \
                    Japanese lung has 4 toes, Indonesian 3, Chinese or Imperial lung has 5 toes.",
        "wyvern": "A largest form of a dragon with 2 legs, 2 wings, \
                    and often a pointed tail which is said to be a venomous stinger. \
                    Muddy brown to lime green in color and 50 feet long.",
        "amphithere": "A type of water dragon from English folklore.",
        "lindworm": "A serpent-like dragon with either two or no legs.",
        "phoenix": "A type of water dragon from English folklore.",
        "marsupial": "A type of water dragon from English folklore.",
        "kirimu": "A type of water dragon from English folklore.",
        "leviathan": "A creature with the form of a sea monster.",
        "bakunawa": "A type of water dragon from English folklore.",
        "imoogi": "A type of water dragon from English folklore.",
        "kihawahine": "A type of water dragon from English folklore.",
        "basilisk": "A type of water dragon from English folklore.",
        "frost": "A type of water dragon from English folklore.",
        "cockatrice": "A type of water dragon from English folklore.",
        "serpent": "A type of water dragon from English folklore.",
        "taniwha": "A huge water lizard in Polynesian mythology. \
                    At sea, a taniwha often appears as a whale \
                    or a large shark such as southern right whale or whale shark. \
                    In inland waters, they may still be of whale-like dimensions, \
                    but look more like a gecko or a tuatara, having a row of spines along back.",
        "uwabami": "A giant serpent or giant python in the legends of Japan.",
        "orochi": "Legendary eight-headed and eight-tailed Japanese dragon/serpent.",
        "zahhak": "A serpent with 3 heads, and 1 of the heads is human."
    }

    while attempts > 0:
        display = display_name(name_to_guess, guessed_letters)
        print(color["orange"].apply_color(f"Name to guess: {display}"))
        guess = input(color["yellow"].apply_color("Guess a letter:\n")).lower()

        if len(guess) != 1 or not guess.isalpha():
            print(color["green"].apply_color("Please enter one letter!"))
            continue

        if guess in guessed_letters:
            print(color["green"].apply_color
                  ("Oh, sorry, you have already guessed that letter!")
                  )
            print(color["green"].apply_color
                  ("Please try again!")
                  )
            continue

        guessed_letters.append(guess)

        if display == name_to_guess:
            print(color["green"].apply_color
                  ("Great guess! You are one step closer to revealing dragon!")
                  )
            print(color["green"].apply_color
                  ("Congrats! You are a true dragon master!")
                  )
            print(color["green"].apply_color
                  (f"You guessed {name_to_guess} dragon!")
                  )

            # Retrieve and display the dragon's description
            if name_to_guess in dragon_descriptions:
                print(color["yellow"].apply_color
                      (f"Description: {dragon_descriptions[name_to_guess]}")
                      )

            break

        if guess not in name_to_guess:
            attempts -= 1
            print(color["green"].apply_color
                  (f"Aw, incorrect! You have {attempts} attempts remaining.")
                  )

    if attempts == 0:
        print(color["green"].apply_color("Sorry, dragon got you!"))
        print("")
        print(color["orange"].apply_color(f"It was {name_to_guess} dragon!"))

        if name_to_guess in dragon_descriptions:
            print(color["yellow"].apply_color
                  (f"{dragon_descriptions[name_to_guess]}")
                  )

    main_logo()


def main():
    """
    Runs all functions in program
    """
    main_logo()
    intro()
    username = enter_username()
    game_rules(username)
    continue_to_game(username)
    start_game(username, DRAGON_LIST)


main()
