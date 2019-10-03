from room import Room
from player import Player
from item import Item
# Import class objects
# Declare all the rooms

# Added a couple rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("lantern", "a small amount of fuel remains.")]),

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

    'pathway': Room("Sunken Pathway", """You notice a shimmering pool to the east, you may be able to swim though.
What could be on the otherside you wonder.""", []),

    'tunnel': Room("Damp Tunnel", """You emerge from the watery pathway and find yourself in a dark passageway. 
You hear a eerie whisper to the north.""", []),

    'throneroom': Room("The Throne Room", """As you walk through the passageway you begin to see torches line the walls, 
you see lights further down. Upon exiting the tunnel you find yourself in what appears to be a throne room. 
Multiple torches remain lit, and there is no source of the whispers you heard.""", [Item("dusty crown", "a thick layer of dust covers the inlaid jewels of this crown.")]),
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
room['treasure'].e_to = room['pathway']
room['pathway'].w_to = room['treasure']
room['pathway'].n_to = room['tunnel']
room['tunnel'].s_to = room['pathway']
room['tunnel'].w_to = room['throneroom']
room['throneroom'].e_to = room['tunnel']
# Link additional rooms.

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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
#------------------------------------------------------------------------------

# Create player, start at the beginning, in the room labeled "outside".
player = Player('Lord Grimm', room['outside'], [Item("Bow", "basic wooden bow")])

# Welcome Message
# Includes instructions for acceptable inputs,
print('\n--------------------------------------------------------------------------------')
print(f'\nWelcome to the Spooky Maze!\n')
print(f'\nAvailable move direction commands: [n], [e], [s], [w]')
print(f'Available item commands: get, take, drop, remove')
print(f'Press [q] to quit the program')
print('\n--------------------------------------------------------------------------------')

# Print player.name & player.room
def current_location(player):
    print(f"\n{player.name}, is currently in the {player.room}. Do you wish to continue?")
    # Print out any available items
    if player.room.items:
        print(f'\n\nYou notice these items in the {player.room.name}.\n')
        for item in player.room.items:
            print(f'{item.name} ---- {item.description}')
    else:
        print(f'\nThere is nothing of value in this room.')
    print('\n-----------------------------------------------------------------------------')

# Create an array using the four moveable directions. 
directions = ['n', 'e', 's', 'w']

# Create a control loop to handle the game.
# Using while true will allow it to run until closed out.
while True:
    # Print out player information as player moves through the game
    current_location(player)
    # Print out available command options
    print('\nChoose a direction: [n]orth, [e]ast, [s]outh, [w]est')
    print('Options: [get][item] [take][item] or [drop][item] [remove][item] or [i] to see inventory')
    print('Press [q] to quit the program')
    user_input = input(">>>>> ").lower()  # use .lower to ensure inputs are brought into a useable format
    print('\n--------------------------------------------------------------------------------')
    new_input = user_input.split(" ")  # Split at the space allowing for more than just cardinal direction inputs.

    # Input controller
    # single argument commands
    if len(new_input) == 1:
        if user_input[0] in directions:  # Check if the input is valid
            player.move(user_input)
        elif user_input[0] == 'i':
            player.view_inventory()
        elif user_input[0] == 'q':
            print(f"\n\nCome back soon, {player.name}. Hope you enjoyed your stay. Exiting game now.")
            break
        else:
            print('\nInvalid input, please choose from the available commands.')
    
    # two argument commands
    elif len(new_input) == 2:
        # take care of picking up items
        if new_input[0] == 'get' or new_input[0] == 'take':
            for item in player.room.items:
                if item.name == new_input[1]:
                    player.pickup(item)
                elif item in [item.name for item in player.room.items] != new_input[1]:
                    print('\nThis item does not appear to be in this room.\n\n')
        # take care of dropping items
        elif new_input[0] == 'drop' or new_input[0] == 'remove':
            for item in player.items:
                if item.name == new_input[1]:
                    player.drop(item)
                elif item in [item.name for item in player.room.items] != new_input[1]:
                    print('\nYou do not possess such an item.')