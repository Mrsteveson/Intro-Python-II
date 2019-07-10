from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Torch", "still usable")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),

    'secret': Room("Secret Hallway", """A light breeze catches your attention,
you find a small hidden passageway. Where might it lead?""", [Item("Gold Key", "has to unlock something?")])

}

    


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].e_to = room['secret']
room['secret'].w_to = room['treasure']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Sir Patty', room['outside'], [Item("Sword", "Basic iron sword")])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print(f'\nWelcome to the Dungeon.')

def location(player):
    print(f'\n{player.name}, is in the {player.room}')

    if player.room.items:
        print(f'\nFound these items in the {player.room.name}')
        for item in player.room.items:
            if item is not None:
                print(f'A {item.name}, {item.description}')
    else:
        print(f'\nNo items found in this area')

playermove = None

while playermove != 'q':
    location(player)

    print('\nChoose a direction')
    playermove = input('[n]orth, [e]ast, [s]outh, [w]est, [q]uit: ')

    if playermove == 'n' or playermove == 'e' or playermove == 's' or playermove == 'w':
        if playermove == 'n' and player.room.n_to:
            player.room = player.room.n_to
        elif playermove == 'e' and player.room.e_to:
            player.room = player.room.e_to
        elif playermove == 's' and player.room.s_to:
            player.room = player.room.s_to
        elif playermove == 'w' and player.room.w_to:
            player.room = player.room.w_to
        else:
            print('\nNo room located in that direction, please choose again.')
    elif playermove == 'q':
        print(f'\nThank you for playing, {player.name}! Exiting Game.')
        break
    else:
        print('\nInvalid input, please choose again.')