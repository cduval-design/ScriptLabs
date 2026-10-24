# Import date module
from datetime import date


# Define header function
def header():
    # "Clear" the screen (not available in IDLE)
    print("\n" * 100)

    print("Name: Duval, McKenna")
    print("Course: ITSY 1375-9P1")
    print("Assignment: Lab 3.5 - Python Flow Control")
    print("Current Date:", date.today())

    print("\n" * 5)


# Import random module
import random

# Save each variable's locations
agents = [[0, 0], [0, 0]]
weapon = [0, 0]
phonebooth = [0, 0]
player = [0, 0]

# Randomize locations and make sure they're different
player = [random.randint(0, 2), random.randint(0, 2)]
while True:
    phonebooth = [random.randint(0, 2), random.randint(0, 2)]
    if phonebooth != player:
        break
while True:
    weapon = [random.randint(0, 2), random.randint(0, 2)]
    if weapon != player and weapon != phonebooth:
        break
while True:
    agents[0] = [random.randint(0, 2), random.randint(0, 2)]
    if agents[0] != player and agents[0] != phonebooth and agents[0] != weapon:
        break
while True:
    agents[1] = [random.randint(0, 2), random.randint(0, 2)]
    if (
        agents[1] != player
        and agents[1] != phonebooth
        and agents[1] != weapon
        and agents[1] != agents[0]
    ):
        break


# Weapon status
has_weapon = False


# Function for game board display
def game_board():
    # Create the 3x3 Matrix grid
    matrix = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    matrix[player[0]][player[1]] = "P"
    for row in matrix:
        print(" ".join(row))


# Function for player movement
def move_space():
    choice = (
        input("\nWhich way would you like to move? (Up/Down/Left/Right): ")
        .strip()
        .lower()
    )
    if choice == "up":
        if player[0] == 0:
            print("Oops! There's a wall there. Try going another direction.")
        else:
            player[0] -= 1
    elif choice == "down":
        if player[0] == 2:
            print(
                "Careful! You almost fell over the edge. Try going another direction."
            )
        else:
            player[0] += 1
    elif choice == "left":
        if player[1] == 0:
            print("Oops! There's a wall there. Try going another direction.")
        else:
            player[1] -= 1
    elif choice == "right":
        if player[1] == 2:
            print(
                "Careful! You almost fell over the edge. Try going another direction."
            )
        else:
            player[1] += 1
    else:
        print("That wasn't one of the options. Choose a valid direction.")


# Function for agent encounter
def encounter_agent():
    if player not in agents:
        return "continue"
    print("\nOh no, there's an agent!")
    if not has_weapon:
        print("\nHe captured you! Too bad you didn't have a weapon...")
        return "defeat"
    print("\nGood thing you have a weapon. Let's hope this works...")
    if random.randint(0, 1) == 1:
        print("\nNice hit! You defeated the agent.")
        agents.remove(player.copy())
        return "continue"
    print("\nThe agent defeated you.")
    return "defeat"


# Function for phonebooth encounter
def encounter_phonebooth():
    if player == phonebooth:
        print("\nYou reached the phone booth and escaped the Matrix!")
        return True
    return False


# Function for weapon encounter
def encounter_weapon():
    global has_weapon
    if player != weapon or has_weapon:
        return
    print("\nYou've found a weapon!")
    while True:
        take_weapon = (
            input("\nWould you like to pick it up? You may need it later!(Y/N): ")
            .strip()
            .upper()
        )
        if take_weapon == "Y":
            has_weapon = True
            print("\nYou picked up the weapon. Smart move!")
            break
        elif take_weapon == "N":
            print("\nYou're leaving it behind. I hope you know what you're doing...")
            break
        else:
            print("\nThat wasn't one of the options. Enter Y or N")


# The Matrix simulation function
def matrix_simulation():
    # Call the header function
    header()

    # Format for the game
    print("\n\n=== Welcome to The Matrix ===\n")
    print("Find your way to the phonebooth!\n")

    game_board()

    while True:
        move_space()
        game_board()
        encounter_weapon()
        agent_result = encounter_agent()
        if agent_result == "defeat":
            print("\nYou did not escape The Matrix.\nGame over.\n")
            break
        if encounter_phonebooth():
            print("You win!\n")
            break


# Start the game
matrix_simulation()
