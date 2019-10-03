# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items):
        self.name = name
        self.room = room
        if items == None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f"Greetings, {self.name}, you are currently in {self.room}."
    # Function to move player throughout maze
    def move(self, direction):
        if getattr(self.room, f"{direction}_to") is not None:
            self.room = getattr(self.room, f"{direction}_to")
        else:
            print("\nThere is no room in that direction, please choose again.")
    # Function to pickup item and add to inventory
    def pickup(self, item):
        if item in self.room.items:
            self.items.append(item)
            self.room.items.remove(item)
            item.on_pickup()
        else:
            print(f'\n{item} does not exist in this room.\n')
    # Function to drop item from inventory and add to the room
    def drop(self, item):
        if item in self.items:
            self.items.remove(item)
            self.room.items.append(item)
            item.on_drop()
        else:
            print(f'\nYou do not possess {item}.\n')

    def view_inventory(self):
        print(f"\n\n{self.name}'s possessions:\n" + "," .join([item.name for item in self.items]))