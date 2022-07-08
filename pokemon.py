# Text based pokemon game, based off of pokemon red and blue

import random
import time

class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Pokemon:
    
    VALID_TYPES = ["FIRE", "GRASS", "WATER"]

    def __init__(self, hp, name, type):
        self.hp = hp
        self.name = name
        self.type = type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if type not in Pokemon.VALID_TYPES:
            raise ValueError("Invalid type.")
        self._type = type

    # Name, e.g. Charmander
    # Type, e.g. Fire, Grass, Water
    # WeakAgainst, e.g. if Grass, fire. if water, grass. if fire, water
    # StrongAgainst, same as above, a list based off of https://www.eurogamer.net/pokemon-go-type-chart-effectiveness-weaknesses
    # if no strong against, go with normal damage type, otherwise use "Super effective" and "Not very effective"

class Charmander(Pokemon):

    ATTACKS = ["Scratch", "Ember"]
    WEAKNESS = "WATER"

    def __init__(self, hp="100", name="Charmander", type="FIRE"):
        super().__init__(hp, name, type)

class Bulbasaur(Pokemon):

    ATTACKS = ["Tackle", "Vine Whip"]
    WEAKNESS = "FIRE"

    def __init__(self, hp="100", name="Bulbasaur", type="GRASS"):
        super().__init__(hp, name, type)

class Squirtle(Pokemon):

    ATTACKS = ["Tackle", "Tail Whip"]
    WEAKNESS = "GRASS"

    def __init__(self, hp="100", name="Squirtle", type="WATER"):
        super().__init__(hp, name, type)

class Person:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name.isalpha():
            raise ValueError("Name must use letters only!\n")
        self._name = name

class Trainer(Person):
    
    def __init__(self, name):
        super().__init__(name)
        self.pokemon_belt = []
    
    def add_pokemon(self, pokemon):
        if not isinstance(pokemon, object):
            raise ValueError("POKéMON must be of object type to add to belt!")
        self.pokemon_belt.append(pokemon)

class Professor(Person):
    pass

# Let the user select from a list
def let_user_pick(options):

    for idx, element in enumerate(options):
        print("{}) {}".format(idx + 1, element))

    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return int(i) - 1
    except:
        pass
    return None

def start_game():
    print(colors.GREEN + "\nHello there! Welcome to the world of POKéMON!\nMy name is Oak! People call me the Pokemon PROF!")
    your_name = input("First, what is your name?\n\n")

    main_character = Trainer(your_name)

    print(f"\nRight! So your name is {main_character.name}!")
    time.sleep(2)
    print(f"\nThis is my grandson. He's been your rival since you were a baby.")
    grandson_name = input("...Erm, what is his name again?\n\n")

    grandson = Trainer(grandson_name)

    print(f"\nThat's right! I remember now! His name is {grandson.name}!\n")
    time.sleep(2)
    print(f"{main_character.name}!")
    print(f"Your very own POKéMON legend is about to unfold!")
    print(f"A world of dreams and adventures with POKéMON awaits! Lets go!\n")

    print(colors.CYAN + f"You pick first! Choose your starter POKéMON:\n")
    options = ["Bulbasaur", "Charmander", "Squirtle"]
    your_selection = let_user_pick(options)

    if options[your_selection] == "Bulbasaur":
        your_pokemon = Bulbasaur()
        main_character.add_pokemon(your_pokemon)
    elif options[your_selection] == "Charmander":
        your_pokemon = Charmander()
        main_character.add_pokemon(your_pokemon)
    elif options[your_selection] == "Squirtle": 
        your_pokemon = Squirtle()
        main_character.add_pokemon(your_pokemon)
    else:
        raise ValueError("Invalid selection.")

    print(colors.GREEN + f"\nYou selected {your_pokemon.name}! {your_pokemon.name} was added to your POKéMON belt.")
    options.remove(your_pokemon.name)

    time.sleep(2)
    print(f"\n{grandson.name}, it's your turn!\n")
    time.sleep(1)
    print(colors.RED + f"{grandson.name}: I'll take this one then!")
    grandson_choice = random.choice(options)
    
    if grandson_choice == "Bulbasaur":
        grandson_pokemon = Bulbasaur()
        grandson.add_pokemon(grandson_pokemon)
    elif grandson_choice == "Charmander":
        grandson_pokemon = Charmander()
        grandson.add_pokemon(grandson_pokemon)
    elif grandson_choice == "Squirtle": 
        grandson_pokemon = Squirtle()
        grandson.add_pokemon(grandson_pokemon)
    else:
        raise ValueError("Invalid selection.")

    time.sleep(2)
    print(colors.CYAN + f"*{grandson.name} received a {grandson_choice}!*\n")

    time.sleep(2)
    print(colors.RED + f"{grandson.name}: Wait, {main_character.name}!")
    time.sleep(1)
    print(f"{grandson.name}: Let's check out our POKéMON!")
    time.sleep(1)
    print(f"{grandson.name}: Come on, I'll take you on!\n")
    time.sleep(1)
    print(colors.RED + f"{grandson.name} challenges you to a duel!", end=" ")
    print(colors.RED + f"{grandson.name} sent out {grandson_choice}!")
    time.sleep(1)
    print(colors.GREEN + f"You sent out {your_pokemon.name}!\n")

    print(colors.CYAN + f"Select Option:")
    options = ["Fight", "Run"]
    your_selection = let_user_pick(options)

    if options[your_selection] == "Fight":
        # Check both types.
        # Possible choices (grandson, you):
        #           water, fire    -> you lose
        #           water, grass   -> you win
        #           grass, fire    -> you win
        #           grass, water   -> you lose
        #           fire, grass    -> you lose
        #           fire, water    -> you win
        if grandson_pokemon.type == your_pokemon.WEAKNESS:
            time.sleep(1)
            print(colors.GREEN + f"\n{your_pokemon.name} used {random.choice(your_pokemon.ATTACKS)}! Not very effective!")
            time.sleep(2)
            print(colors.RED + f"Enemy {grandson_pokemon.name} used {random.choice(grandson_pokemon.ATTACKS)}. It was super effective!")
            time.sleep(2)
            print(colors.RED + f"Your {your_pokemon.name} fainted. You lose!\n")
            exit
        elif your_pokemon.type == grandson_pokemon.WEAKNESS:
            time.sleep(1)
            print(colors.GREEN + f"\n{your_pokemon.name} used {random.choice(your_pokemon.ATTACKS)}! Critical hit!")
            time.sleep(2)
            print(colors.RED + f"Enemy {grandson_pokemon.name} fainted. You Win!\n")
            exit
    elif options[your_selection] == "Run":
        print(f"\nYou ran away. You lose!\n")
        exit

start_game()
