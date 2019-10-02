from room import Room
from player import Player
from item import Item
# Import class objects
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
# print(f'Available item commands: get, take, drop, remove')
print(f'Press [q] to quit the program')
print('\n--------------------------------------------------------------------------------')

# Print player.name & player.room
def current_location(player):
    print(f"\n\n\n{player.name}, is currently in the {player.room}. Do you wish to continue?")
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
    print('Press [q] to quit the program')
    user_input = input(">>>>> ").lower()  # use .lower to ensure inputs are brought into a useable format
    print('\n--------------------------------------------------------------------------------')
    new_input = user_input.split(" ")  # Split at the space allowing for more than just cardinal direction inputs.
    # Input controller
    if len(new_input) == 1:
        if user_input[0] in directions:  # Check if the input is valid
            player.move(user_input)
        elif user_input[0] == 'q':
            print(f"\n\nCome back soon, {player.name}. Hope you enjoyed your stay. Exiting game now.")
            break
        else:
            print('\nInvalid input, please choose from the available commands.')
